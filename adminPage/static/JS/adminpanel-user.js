//labels si label vor fi modificate manual
//daca datele vor fi mai multe de 12,mai apoi voi modifica in js cate trebuie
//am utilizat librarie chart.js, ca sa lucreze,puneti va rog undeva mapa js-lib-plot (va trebui de schimbat directoriul in html )
//<script src="../js-lib-plot/chart.js/dist/Chart.js"></script> asa arat randul care se va modifica

let data1 = [1, 2, 10, 4, 5, 6, 7, 8, 9, 10, 11, 12];
let data2 = [1, 2, 10, 4, 5, 6, 7, 8, 9, 10, 11, 12];
let data3 = [1, 2, 10, 4, 5, 6, 7, 8, 9, 10, 11, 12];
let data4 = [1, 2, 10, 4, 5, 6, 7, 8, 9, 10, 11, 12];
let name = "Name";
let age = "18";
let gender = "Male";
let region = "Republic of Moldova";
let height = "180";
let weight = "70";
let disease = ["Some disease", "Some disease"];

document.getElementById("user-name").innerHTML = name;
document.getElementById("user-age").innerHTML = age;
document.getElementById("user-gender").innerHTML = gender;
document.getElementById("user-region").innerHTML = region;
document.getElementById("user-height").innerHTML = height + " cm";
document.getElementById("user-weight").innerHTML = weight + " kg";
document.getElementById("user-disease").innerHTML = disease;
new Chart(document.getElementById("line-chart1"), {
  type: "line",
  data: {
    labels: [
      "January",
      "February",
      "March",
      "April",
      "May",
      "June",
      "July",
      "August",
      "September",
      "October",
      "November",
      "December",
    ],
    datasets: [
      {
        data: [
          data1[0],
          data1[1],
          data1[2],
          data1[3],
          data1[4],
          data1[5],
          data1[6],
          data1[7],
          data1[8],
          data1[9],
          data1[10],
          data1[11],
        ],
        label: "Hours slept",
        borderColor: "#3e95cd",
        fill: false,
      },
    ],
  },
  options: {},
});
new Chart(document.getElementById("line-chart2"), {
  type: "line",
  data: {
    labels: [
      "January",
      "February",
      "March",
      "April",
      "May",
      "June",
      "July",
      "August",
      "September",
      "October",
      "November",
      "December",
    ],
    datasets: [
      {
        data: [
          data2[0],
          data2[1],
          data2[2],
          data2[3],
          data2[4],
          data2[5],
          data2[6],
          data2[7],
          data2[8],
          data2[9],
          data2[10],
          data2[11],
        ],
        label: "Hours slept",
        borderColor: "#3e95cd",
        fill: false,
      },
    ],
  },
  options: {},
});
new Chart(document.getElementById("line-chart3"), {
  type: "line",
  data: {
    labels: [
      "January",
      "February",
      "March",
      "April",
      "May",
      "June",
      "July",
      "August",
      "September",
      "October",
      "November",
      "December",
    ],
    datasets: [
      {
        data: [
          data3[0],
          data3[1],
          data3[2],
          data3[3],
          data3[4],
          data3[5],
          data3[6],
          data3[7],
          data3[8],
          data3[9],
          data3[10],
          data3[11],
        ],
        label: "Hours slept",
        borderColor: "#3e95cd",
        fill: false,
      },
    ],
  },
  options: {},
});
new Chart(document.getElementById("line-chart4"), {
  type: "line",
  data: {
    labels: [
      "January",
      "February",
      "March",
      "April",
      "May",
      "June",
      "July",
      "August",
      "September",
      "October",
      "November",
      "December",
    ],
    datasets: [
      {
        data: [
          data4[0],
          data4[1],
          data4[2],
          data4[3],
          data4[4],
          data4[5],
          data4[6],
          data4[7],
          data4[8],
          data4[9],
          data4[10],
          data4[11],
        ],
        label: "Hours slept",
        borderColor: "#3e95cd",
        fill: false,
      },
    ],
  },
  options: {},
});
