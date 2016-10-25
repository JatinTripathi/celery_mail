from flask import send_from_directory
from flask import render_template

from goals import app
from goals.models import LifeGoal

brief_description_max = 10


@app.route('/api/home/static/<path:path>')
def send_static(path):
    try: return send_from_directory('static', path)

    except Exception ,e:
        logging(e)


@app.route("/api/home/")
def home():
    try: return render_template('home.html')

    except Exception ,e:
        logging(e)


@app.route("/api/goal/", methods=['GET', 'POST'])
def goal(request):
    try:
        if (request.method == 'GET'):
            goal_type = request.args.get('type')
            all_goals = []
            goals = LifeGoal.objects.all()

            for goal in goals:
                if str(goal.completed) == goal_type:
                    days_left = make_naive(goal.end_date, timezone=None) - datetime.datetime.now()
                    if goal.rest_description: more = '... More'
                    else: more = ''
                    data = {'id':goal.id, 
                            'name': goal.name, 
                            'text':goal.brief_description, 
                            'date':days_left.days, 
                            'complete':str(goal.completed),
                            'more': more}
                    all_goals.append(data)
                    
            return JsonResponse(all_goals, safe=False)
        
        if (request.method == 'POST'):
            data = request.form

            a = data['end_date'].decode('utf-8')
            end_date = datetime.datetime.strptime(a, '%Y-%m-%d')

            description_words_array = data['description'].split()
            if len(description_words_array) > brief_description_max:
                brief_description = ' '.join(description_words_array[:brief_description_max])
                rest_description = ' '.join(description_words_array[brief_description_max:])
            else:
                brief_description = data['description']
                rest_description = None
            
            goal = LifeGoal(name = data['name'], 
                            brief_description = brief_description,
                            rest_description = rest_description, 
                            end_date = end_date,
                            completed = False)
            goal.save()
            
            return JsonResponse({'message': 'Saved'}, safe=False)

    except Exception ,e:
        logging(e)


def logging(err):
    print err