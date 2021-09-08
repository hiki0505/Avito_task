# Тестовое задание по python

## Описание проекта

Программа, которая осуществляет получение квадратной матрицы (NxN) с удалённого сервера и возвращает её пользователю в виде листа.
Этот список содержит результат обхода полученной матрицы по спирали: против часовой стрелки, начиная с левого верхнего угла.

Программа реализована засчёт библиотеки FastAPI, в которую уже встроены асинхронные методы и функции.
Для работы этой программы необходимо иметь следующие зависимости (установленные модули):

<img align="left" alt="Urrlib3" width="80px" length="30" src="https://user-images.githubusercontent.com/49026411/132472837-f96af8e6-2e99-4e40-b949-4d23247982c2.png" /> 
<img align="left" alt="Aiohttp" width="52px" length="30" src="https://user-images.githubusercontent.com/49026411/132473000-ca5c35ab-46ca-487f-aea4-9999c98c4081.jpeg" /> 
<img align="left" alt="Fastapi" width="80px" length="30" src="https://user-images.githubusercontent.com/49026411/132472315-32b2efc8-8bb7-4701-8665-f910bde5cfed.png" /> 
<img align="left" alt="Pytest" width="80px" length="30" src="https://user-images.githubusercontent.com/49026411/132473169-00a1be60-0224-4bef-aee4-976e877cfc73.png" /> </br></br>
</br>



Программа покрыта тестом, проверяющая соответствие ожидаемого и реального результата.

Инструкции к выполнению:

#### 1) Скачиваем зависимости, используя 
```shell 
pip install -r requirements.txt 
```
#### 2.1) Для проверки работы API, вводим в терминале команду ```uvicorn api:app --reload```, затем переходим по ссылке http://127.0.0.1:8000/docs, нажимаем на GET, передаём в поле <i> url </i> виде параметра ссылку на матрицу, и получаем спиральный массив. Ну или же более простой метод: в адресной строке вводим http://127.0.0.1:8000/get_matrix/?url=<ссылка на текстовую матрицу с сервера> и получаем результат.


#### 2.2) Для проверки работы теста, в файле <i> main_test.py </i> в поле SOURCE_URL вставляем ссылку на текстовую матрицу с удалённого сервера, а также в поле TRAVERSAL матрицу, которую ожидаете получить. Затем в терминале вводим простую команду ```pytest```. Если тест прошёл успешно, будет возвращён сигнал '1 passed', в противном случае тест провалится.



