from invoke import run, task


@task
def build(context):
    context.run("docker compose --env-file app/.env build")
    print("Build done...")


@task
def up(context):
    context.run("docker compose --env-file app/.env up -d")
    print("Running services...")


@task
def update_deps(context):
    context.run("rm -f app/requirements.txt")
    context.run("pip freeze > app/requirements.txt")
    print("Updated app/requirements.txt")


@task
def gen_schemas(context):
    input_dir = "app/schemas/json_schemas"
    output_dir = "app/schemas/policy_schemas"
    filenames = [
        {
            "input_file": "policy_schema_qoe_and_tsp.json",
            "output_file": "qoeandtspv2.py",
        },
        {
            "input_file": "policy_schema_qoe_target.json",
            "output_file": "qoetargetv2.py",
        },
        {
            "input_file": "policy_schema_qos_and_tsp.json",
            "output_file": "qosandtspv2.py",
        },
        {
            "input_file": "policy_schema_qos_target.json",
            "output_file": "qostargetv2.py",
        },
        {
            "input_file": "policy_schema_slice_sla_target.json",
            "output_file": "sliceslatargetv1.py",
        },
        {
            "input_file": "policy_schema_traffic_steering_preference.json",
            "output_file": "tspv2.py",
        },
        {
            "input_file": "policy_schema_ue_level_target.json",
            "output_file": "ueleveltargetv1.py",
        },
    ]

    for file in filenames:
        context.run(
            f"datamodel-codegen  --input {input_dir}/{file.get('input_file')} --input-file-type jsonschema --output {output_dir}/{file.get('output_file')}"
        )

    print("Generate Done...")
