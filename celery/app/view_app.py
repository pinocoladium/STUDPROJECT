import os
import uuid

from celery.result import AsyncResult
from celery_app import celery_app, upscale_image
from flask import jsonify, request
from flask.views import MethodView


class Upscale(MethodView):
    def get(self, task_id):
        task = AsyncResult(task_id, app=celery_app)
        return jsonify({"status": task.status, "result": task.result})

    def post(self):
        task = upscale_image.delay(self.save_image("image_before"), os.path.join('result_image', f'{uuid.uuid4()}'))
        return jsonify({"task_id": task.id})

    def save_image(self, field):
        image = request.files.get(field)
        extension = image.filename.split('.')[-1]
        path = os.path.join('files', f'{uuid.uuid4()}.{extension}')
        image.save(path)
        return path