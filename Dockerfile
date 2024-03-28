FROM python:3.10

# Copy the code
WORKDIR /app
COPY . .

RUN mkdir -p /app/test-reports/

RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple 

# Run tests
CMD ["python", "src/entrypoint.py"]
# export report

#RUN chmod +x infinite_loop.sh
#CMD ["./infinite_loop.sh"]
