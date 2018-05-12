FROM postgres:latest
# RUN groupadd -r user_postgres &&\
# 	useradd --no-log-init -r -g user_postgres user_postgres
# ARG path=/var/lib/postgresql/data
# RUN chown -R user_postgres:user_postgres $path
# USER user_postgres

RUN useradd foo
RUN mkdir /data && touch /data/x
RUN chown -R foo:foo /data
VOLUME /data