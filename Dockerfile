FROM python:3.6.8

ENV home_dir=/opt/redis_data/
RUN mkdir -p ${home_dir}
WORKDIR ${home_dir}

COPY Pipfile* ./
RUN pip install --upgrade pip && pip install pipenv 
RUN pipenv install --system --dev
COPY ./ ./

EXPOSE 5000
EXPOSE 8888

ENTRYPOINT ["devops/entrypoint.sh"]