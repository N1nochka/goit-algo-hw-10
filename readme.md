# Висновки:

Отримані результати показують, що значення інтегралу, обчисленого методом Монте-Карло (2.6346696995057592), дещо відрізняється від значення, отриманого за допомогою функції quad (2.6666666666666665). Похибка обчислення, яка становить 0.031996967160907275, підтверджує цю відмінність.

Зазначена різниця між результатами виникає через природу кожного методу обчислення інтегралу. Метод Монте-Карло базується на випадковому виборі точок у просторі і оцінює значення інтегралу шляхом вимірювання відсотка точок, що потрапляють під криву, відносно загальної кількості випадкових точок. З іншого боку, функція quad використовує чисельні методи для точного обчислення значення інтегралу.

Загалом, результати методу Монте-Карло можуть збігатися з точним значенням інтегралу лише у випадку великої кількості випадкових точок. У цьому конкретному випадку різниця між обчисленими значеннями інтегралу може бути прийнятною з урахуванням відносної похибки.