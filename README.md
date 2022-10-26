# moring_test
1. 비어있는 폴더를 만들어주세요
2. 가상환경을 만들고 실행해주세요
3. `django`와 `djangorestframework`를 설치해주세요
4. (선택) .gitignore 추가 및 `pip freeeze > requirements.txt`
5. morning_quiz  프로젝트를 만들어주세요.
6. `rest_framework`를 INSTALLED_APPS에 등록하세요
7. articles 앱을 생성 후 INSTALLED_APPS에 등록 후 아래와 같은 model을 만들어주세요.
    
    ```bash
    class Article(models.Model):
    	title = models.CharField(max_length=100)
    	content = models.TextField()
    ```
    
8. 모델을 DB에 반영해주세요
9. articles의 index라는 함수에 url을 연결해주세요. (경로는 무방)
10. [serializers.py](http://serializers.py) 를 생성 후 아래와 같이 ModelSerializer를 정의해주세요.
    
    ```bash
    from rest_framework import serializers
    from articles.models import Article
    
    class ArticleSerializer(serializers.ModelSerializer):
    	class Meta:
    		model = Article
    		fields = '__all__'
    ```
    
    > **serializer의 의미가 무엇인지 답안 해설 때 한 명 콕 집에서 물어볼 예정입니다**
    > 
11. views.py의 index 함수에 아래와 같이 동작하도록 구현해보세요.
