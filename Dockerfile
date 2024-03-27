FROM python:3.9



# Copy the code
WORKDIR /usr/src/app
COPY . .

# Run tests
#CMD ["python", "api-test-framework\entrypoint.py"]

# export report


RUN chmod +x infinite_loop.sh
CMD ["./infinite_loop.sh"]