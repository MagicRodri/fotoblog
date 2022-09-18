from email import message
import json

from channels.generic import websocket
from asgiref.sync import async_to_sync

class CommentConsumer(websocket.WebsocketConsumer):

    def connect(self):

        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

        self.send(text_data=json.dumps({
            'type' :  'connection_established',
            'message' : 'You are connected to the socket'
        }))

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = f"{text_data_json['username']} : {text_data_json['content']}"

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type' : 'comment_message',
                'message' : message
            }
        )

    def comment_message(self,event):
        message = event['message']
        self.send(text_data=json.dumps({
            'type' : 'comment',
            'message' : message
        }))
