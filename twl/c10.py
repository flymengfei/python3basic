# -*- coding: utf-8 -*-

@api.route('/get',methods=['GET'])
def test_javascript_http():
    p = request.args.get('name')
    return p,200

# flask

@api.route('/psw',methods=['GET'])
@auth.login_required
def get_psw():
    p = request.args.get('psw')
    r = generate_password_hash(p)
    return 'aaaaaa',200