from transformers import pipeline

# Memuat model untuk question-answering
qa_pipeline = pipeline("question-answering")

# Data teks yang besar (misalnya, diambil dari berbagai sumber)
context = """
1. Hukum Newton Pertama menyatakan bahwa sebuah objek akan tetap dalam keadaan diam atau bergerak lurus dengan kecepatan konstan jika tidak ada gaya yang bekerja padanya.
2. Rumus Pythagoras menjelaskan hubungan antara panjang sisi-sisi segitiga siku-siku: kuadrat dari panjang sisi miring sama dengan jumlah kuadrat dari panjang kedua sisi lainnya.
3. Sel adalah unit dasar kehidupan; semua organisme hidup terdiri dari sel.
4. Proses fotosintesis terjadi di tumbuhan, di mana mereka menggunakan cahaya matahari, air, dan karbon dioksida untuk memproduksi makanan.
5. Teori evolusi menjelaskan bagaimana spesies berubah seiring waktu melalui proses seleksi alam.
"""

# Fungsi untuk menjawab pertanyaan dari teks
def answer_question(question):
    result = qa_pipeline(question=question, context=context)
    return result['answer']

# Contoh penggunaan
question = "Apa hukum Newton pertama?"
answer = answer_question(question)
print(f"Pertanyaan: {question}\nJawaban: {answer}")
