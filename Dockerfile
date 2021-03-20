FROM python:3.8

ENV TARGET /home/polina/python/lab1

WORKDIR "${TARGET}"

COPY main.py "${TARGET}"

COPY requirements.txt "${TARGET}"

RUN set -ex \ 
	pip3 install --no-cache-dir -r requirements.txt \
	&& rm requirements.txt

CMD ["python", "main.py"]

