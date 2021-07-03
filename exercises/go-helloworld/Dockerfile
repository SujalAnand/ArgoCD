FROM  golang:alpine
LABEL "Maintainer" = "Sujal Anand"
COPY . /go/src/app
WORKDIR /go/src/app
RUN go build -o helloworld
EXPOSE 6111
CMD ["./helloworld"]
