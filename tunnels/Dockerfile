FROM alpine:3.2

RUN apk add --update openssh-client && rm -rf /var/cache/apk/*

CMD ssh -vv -NL *:$LOCAL_PORT:$REMOTE_IP:$REMOTE_PORT $REMOTE_USER@$REMOTE_HOST
