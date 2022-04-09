from flask import Flask
from flask import render_template
from flask import request
import io, os, uuid, time

app = Flask(__name__,
            template_folder="../frontend/dist",
            static_folder="../frontend/dist/static")

# Call z3 to resolve the input file
def get_z3_result(input):
    uuid_str = str(uuid.uuid4())
    tmp_file_name = 'tmpfile_%s.txt' %(uuid_str)
    f = open(tmp_file_name, 'w')
    f.write(input)
    f.close()
    cmd = 'z3 %s' %(tmp_file_name)
    start = time.time()
    r = os.popen(cmd)
    output = r.read()
    r.close()
    end = time.time()
    run_time = str((float(end - start)))
    os.system('rm %s' %(tmp_file_name))
    return (output, run_time)


# 主页面
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


# Generate z3 interface
@app.route('/z3/output/generate', methods=["POST"])
def z3():
    input = request.json.get("z3input")
    timeout = request.json.get("timeout")
    print(timeout)
    (output, time) = get_z3_result(input)
    return (output, time)

if __name__ == "__main__":
    app.run(debug=False, port=3000)

