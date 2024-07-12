from google.cloud import firestore

class FirestoreManager:
    def __init__(self):
        self.db = firestore.Client()

    def get_user_data(self, user_id):
        # Firestore'dan kullanıcı verilerini getirme işlemleri
        user_ref = self.db.collection('users').document(user_id)
        user_data = user_ref.get().to_dict()
        return user_data

    def save_user_data(self, user_id, data):
        # Firestore'a kullanıcı verilerini kaydetme işlemleri
        user_ref = self.db.collection('users').document(user_id)
        user_ref.set(data)

    def list_users(self):
        # Firestore'daki tüm kullanıcıları listeleme işlemi
        users_ref = self.db.collection('users')
        users = users_ref.stream()
        user_list = [user.to_dict() for user in users]
        return user_list

    def query_users_by_condition(self, condition_field, condition_value):
        # Belirli bir koşula uyan kullanıcıları sorgulama işlemi
        users_ref = self.db.collection('users')
        query = users_ref.where(condition_field, '==', condition_value)
        result = query.stream()
        matching_users = [user.to_dict() for user in result]
        return matching_users

    def update_user_data(self, user_id, update_data):
        # Kullanıcı verilerini güncelleme işlemi
        user_ref = self.db.collection('users').document(user_id)
        user_ref.update(update_data)