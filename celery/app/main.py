from celery_app import celery_app
from flask import Flask
from view_app import Upscale

app_name = "app"
app = Flask(app_name)
app.config["UPLOAD_FOLDER"] = "files"

celery_app.conf.update(app.config)

class ContextTask(celery_app.Task):
    def __call__(self, *args, **kwargs):
        with app.app_context():
            return self.run(*args, **kwargs)


celery_app.Task = ContextTask


upscale_view = Upscale.as_view("upscale")
app.add_url_rule(
    "/upscale/<string:task_id>", view_func=upscale_view, methods=["GET"]
)
app.add_url_rule("/upscale/", view_func=upscale_view, methods=["POST"])
    
# if __name__ == "__main__":
#     app.run()
    
    
from upscale.upscale import example

print(example())