# use huggingface official image for transformers
FROM huggingface/transformers-pytorch-cpu:4.4.2

# run command to force transformers to pre-download model
RUN python3 -c "from transformers import pipeline; print(pipeline('sentiment-analysis')('Awesome, it worked!'))"

# install flask, transformers is already taken care of
RUN pip install flask

# create directory for our code, and switch to it inside image
WORKDIR  /app

# copy in our app
COPY ./main.py .

# environment variable to tell flask what to run (others are needed for flask...)
ENV FLASK_APP=main.py
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# make port 4242 visible outside the container
EXPOSE 4242

# Command to run
CMD ["flask", "run", "--port", "4242", "--host", "0.0.0.0"]
