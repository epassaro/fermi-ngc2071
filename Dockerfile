 # syntax=docker/dockerfile:1
FROM condaforge/mambaforge
LABEL MAINTAINER="epassaro15@gmail.com"

COPY conda-linux-64.lock /tmp
RUN mamba create -n fermipy --file /tmp/conda-linux-64.lock

RUN conda run -n fermipy pip install git+https://github.com/ldivenere/fermipy.git@431-plsec4 \
    && echo "conda activate fermipy" >> ~/.bashrc

RUN mkdir -p /workdir
COPY data/* /workdir/
WORKDIR /workdir

RUN bash wget.txt
RUN ls *PH*.fits > events.txt
RUN mv *SC*.fits spacecraft.fits
RUN wget https://fermi.gsfc.nasa.gov/ssc/data/access/lat/12yr_catalog/gll_psc_v30.fit
RUN wget https://fermi.gsfc.nasa.gov/ssc/data/analysis/software/aux/4fgl/gll_iem_v07.fits
RUN wget https://fermi.gsfc.nasa.gov/ssc/data/analysis/software/aux/iso_P8R3_SOURCE_V3_v1.txt

COPY config/* notebooks/* scripts/* /workdir/

RUN conda clean --all \
    && apt-get autoremove --purge -y \
    && rm -rf /var/lib/apt/lists/* \
    && rm /tmp/conda-linux-64.lock

ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "fermipy", "/bin/bash", "-c"]
CMD ["jupyter notebook --notebook-dir='/workdir' --ip='*' --no-browser --allow-root"]
