function quickSort(array, lowIndex, highIndex) {
    if (lowIndex >= highIndex) {
        return;
    }
    const pivot = array[highIndex];
    let lp = lowIndex;
    let rp = highIndex;
    while (lp < rp) {
        while (array[lp] <= pivot && lp < rp) {
            lp++
        }
        while (array[rp] >= pivot && lp < rp) {
            rp--;
        }
        swap(array, lp, rp);
    }
    swap(array, lp, highIndex);

    quickSort(array, lowIndex, lp - 1);
    quickSort(array, lp + 1, highIndex);
}

function swap(array, i, j) {
    const tmp = array[i];
    array[i] = array[j];
    array[j] = tmp;
}