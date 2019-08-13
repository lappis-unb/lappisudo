FROM pablodiegoss/coach:boilerplate

COPY ./coach/config /coach/config
COPY ./coach/data /coach/data

RUN make train

RUN ./compress_models.sh

CMD ["nginx", "-g", "daemon off;"]
