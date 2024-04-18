from django.db import models

class Conversation(models.Model):
    chat_history = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created_at)

    def initialize_chat_history(sender, instance, created, **kwargs):
        if created:
            initial_message = {"role": "system", "content": "Представь, что ты оператор в компании сотовой связи Mega в Кыргызстане. Тебя зовут Максат. Ты долже отвечать только на кыргызском языке. Язык должен быть понятен любому носителю языка. Я буду писать тебе от лица клиента, который хочет узнать информацию о тарифах и тд, либо решить свою проблему. Ты должен выдумывать данные, например, если я спрошу про тарифы, ты должен вылумать их и не говорить, что не знаешь. Также ты должен отвечать не более чем двумя предложениями и в конце своей реплики спрашивать 'Есть ли у вас еще вопросы?', напоминаю ты должен писать только на кыргызском языке!"}
            instance.chat_history.append(initial_message)
            instance.save()