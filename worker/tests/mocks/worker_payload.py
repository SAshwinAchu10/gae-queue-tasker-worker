import json
valid_task_data = json.dumps({
	"relative_uri":"/consme-task",
	"project":"api-alien",
	"location":"us-central1",
	"queue":"hello-test",
	"body":"Hello alien"
})

invalid_projectid_task_data = json.dumps({
	"relative_uri":"/consme-task",
	"project":"invalid_id",
	"location":"us-central1",
	"queue":"hello-test",
	"body":"Hello alien"
})

invalid_location_task_data = json.dumps({
	"relative_uri":"/consme-task",
	"project":"api-alien",
	"location":"us-wrong",
	"queue":"hello-test",
	"body":"Hello alien"
})

invalid_queue_task_data = json.dumps({
	"relative_uri":"/consme-task",
	"project":"api-alien",
	"location":"us-wrong",
	"queue":"not-exists",
	"body":"Hello alien"
})

invalid_body_task_data = json.dumps({})