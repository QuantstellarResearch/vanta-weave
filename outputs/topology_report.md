# Topology Analysis Report

This analysis is graph-topology-based and heuristic-first.
It is not a physical AC power-flow simulation or an N-1 study.

Run Dir: D:\workspace\vanta-quantum\outputs
Scenario: Baseline
Selected Candidates: 22
Candidate Count: 50

## Metrics
{
  "centrality_metrics": {
    "average_degree_centrality": 0.024047515572939302,
    "max_degree_centrality": 0.07692307692307693,
    "average_betweenness_centrality": 0.03945810667026331,
    "max_betweenness_centrality": 0.35831231348472714
  },
  "efficiency_metrics": {
    "average_shortest_path_length": 118.0,
    "graph_density": 0.024047515572939302,
    "network_efficiency_score": 0.0002037925048554178
  },
  "robustness_metrics": {
    "resilience_score": 0.012023757786469651,
    "congestion_stability_score": 0.8714157766843085,
    "critical_edge_ratio": 0.0783132530120482,
    "articulation_point_ratio": 0.11016949152542373
  },
  "expansion_metrics": {
    "average_expansion_capacity": 11880.0,
    "average_expansion_cost_efficiency": 3096.434466440179,
    "average_resilience_gain": 0.3181818181818182,
    "average_relief_score": 3096434.466440179
  }
}

## Congestion
{
  "edge_states": [
    {
      "edge_id": 0,
      "from_node": "0",
      "to_node": "1",
      "utilization_ratio": 0.02955236853541938,
      "congestion_score": 0.007388092133854845,
      "critical": false
    },
    {
      "edge_id": 1,
      "from_node": "0",
      "to_node": "2",
      "utilization_ratio": 0.03167704862620117,
      "congestion_score": 0.007919262156550292,
      "critical": false
    },
    {
      "edge_id": 11,
      "from_node": "1",
      "to_node": "11",
      "utilization_ratio": 0.08769134192863005,
      "congestion_score": 0.021922835482157513,
      "critical": false
    },
    {
      "edge_id": 3,
      "from_node": "2",
      "to_node": "4",
      "utilization_ratio": 0.009747314832060589,
      "congestion_score": 0.002436828708015147,
      "critical": false
    },
    {
      "edge_id": 12,
      "from_node": "11",
      "to_node": "2",
      "utilization_ratio": 0.0906783110172941,
      "congestion_score": 0.022669577754323524,
      "critical": false
    },
    {
      "edge_id": 2,
      "from_node": "3",
      "to_node": "4",
      "utilization_ratio": 0.002607561929595828,
      "congestion_score": 0.000651890482398957,
      "critical": false
    },
    {
      "edge_id": 8,
      "from_node": "10",
      "to_node": "3",
      "utilization_ratio": 0.05765609155439663,
      "congestion_score": 0.014414022888599158,
      "critical": false
    },
    {
      "edge_id": 4,
      "from_node": "4",
      "to_node": "5",
      "utilization_ratio": 0.01813221304746726,
      "congestion_score": 0.004533053261866815,
      "critical": false
    },
    {
      "edge_id": 9,
      "from_node": "10",
      "to_node": "4",
      "utilization_ratio": 0.06797251712505935,
      "congestion_score": 0.016993129281264837,
      "critical": false
    },
    {
      "edge_id": 5,
      "from_node": "5",
      "to_node": "6",
      "utilization_ratio": 0.04386981505625578,
      "congestion_score": 0.010967453764063944,
      "critical": false
    },
    {
      "edge_id": 13,
      "from_node": "11",
      "to_node": "6",
      "utilization_ratio": 0.10123617750736376,
      "congestion_score": 0.02530904437684094,
      "critical": false
    },
    {
      "edge_id": 6,
      "from_node": "7",
      "to_node": "8",
      "utilization_ratio": 0.008112414892075908,
      "congestion_score": 0.002028103723018977,
      "critical": false
    },
    {
      "edge_id": 33,
      "from_node": "29",
      "to_node": "7",
      "utilization_ratio": 0.010430247718383311,
      "congestion_score": 0.002607561929595828,
      "critical": false
    },
    {
      "edge_id": 7,
      "from_node": "8",
      "to_node": "9",
      "utilization_ratio": 0.004635665652614805,
      "congestion_score": 0.0011589164131537012,
      "critical": false
    },
    {
      "edge_id": 10,
      "from_node": "10",
      "to_node": "11",
      "utilization_ratio": 0.026899277746735357,
      "congestion_score": 0.006724819436683839,
      "critical": false
    },
    {
      "edge_id": 14,
      "from_node": "10",
      "to_node": "12",
      "utilization_ratio": 0.16111766450749493,
      "congestion_score": 0.04027941612687373,
      "critical": false
    },
    {
      "edge_id": 15,
      "from_node": "11",
      "to_node": "13",
      "utilization_ratio": 0.168302946269048,
      "congestion_score": 0.042075736567262,
      "critical": false
    },
    {
      "edge_id": 18,
      "from_node": "11",
      "to_node": "15",
      "utilization_ratio": 0.22280306009119596,
      "congestion_score": 0.05570076502279899,
      "critical": false
    },
    {
      "edge_id": 170,
      "from_node": "11",
      "to_node": "116",
      "utilization_ratio": 0.060263653483992465,
      "congestion_score": 0.015065913370998116,
      "critical": false
    },
    {
      "edge_id": 16,
      "from_node": "12",
      "to_node": "14",
      "utilization_ratio": 0.20921269565337322,
      "congestion_score": 0.052303173913343305,
      "critical": false
    },
    {
      "edge_id": 17,
      "from_node": "13",
      "to_node": "14",
      "utilization_ratio": 0.21581851920834977,
      "congestion_score": 0.05395462980208744,
      "critical": false
    },
    {
      "edge_id": 19,
      "from_node": "14",
      "to_node": "16",
      "utilization_ratio": 0.12846964711371486,
      "congestion_score": 0.032117411778428716,
      "critical": false
    },
    {
      "edge_id": 24,
      "from_node": "14",
      "to_node": "18",
      "utilization_ratio": 0.09483623720911853,
      "congestion_score": 0.023709059302279633,
      "critical": false
    },
    {
      "edge_id": 40,
      "from_node": "14",
      "to_node": "32",
      "utilization_ratio": 0.41201272048729654,
      "congestion_score": 0.10300318012182413,
      "critical": false
    },
    {
      "edge_id": 20,
      "from_node": "15",
      "to_node": "16",
      "utilization_ratio": 0.2697391748239208,
      "congestion_score": 0.0674347937059802,
      "critical": false
    },
    {
      "edge_id": 21,
      "from_node": "16",
      "to_node": "17",
      "utilization_ratio": 0.04997651438329396,
      "congestion_score": 0.01249412859582349,
      "critical": false
    },
    {
      "edge_id": 35,
      "from_node": "16",
      "to_node": "30",
      "utilization_ratio": 0.21626998237167774,
      "congestion_score": 0.054067495592919436,
      "critical": false
    },
    {
      "edge_id": 165,
      "from_node": "112",
      "to_node": "16",
      "utilization_ratio": 0.18295113549350842,
      "congestion_score": 0.045737783873377104,
      "critical": false
    },
    {
      "edge_id": 22,
      "from_node": "17",
      "to_node": "18",
      "utilization_ratio": 0.046499765143833034,
      "congestion_score": 0.011624941285958259,
      "critical": false
    },
    {
      "edge_id": 23,
      "from_node": "18",
      "to_node": "19",
      "utilization_ratio": 0.0702303346371143,
      "congestion_score": 0.017557583659278574,
      "critical": false
    },
    {
      "edge_id": 41,
      "from_node": "18",
      "to_node": "33",
      "utilization_ratio": 0.17032822795534694,
      "congestion_score": 0.042582056988836735,
      "critical": false
    },
    {
      "edge_id": 25,
      "from_node": "19",
      "to_node": "20",
      "utilization_ratio": 0.07109952194697958,
      "congestion_score": 0.017774880486744894,
      "critical": false
    },
    {
      "edge_id": 26,
      "from_node": "20",
      "to_node": "21",
      "utilization_ratio": 0.09601622482978414,
      "congestion_score": 0.024004056207446035,
      "critical": false
    },
    {
      "edge_id": 27,
      "from_node": "21",
      "to_node": "22",
      "utilization_ratio": 0.13078371722439516,
      "congestion_score": 0.03269592930609879,
      "critical": false
    },
    {
      "edge_id": 28,
      "from_node": "22",
      "to_node": "23",
      "utilization_ratio": 0.7283935148341932,
      "congestion_score": 0.1820983787085483,
      "critical": false
    },
    {
      "edge_id": 29,
      "from_node": "22",
      "to_node": "24",
      "utilization_ratio": 0.10459245713482988,
      "congestion_score": 0.02614811428370747,
      "critical": false
    },
    {
      "edge_id": 37,
      "from_node": "22",
      "to_node": "31",
      "utilization_ratio": 0.5276109954076048,
      "congestion_score": 0.1319027488519012,
      "critical": false
    },
    {
      "edge_id": 99,
      "from_node": "23",
      "to_node": "69",
      "utilization_ratio": 0.7324497222802311,
      "congestion_score": 0.18311243057005777,
      "critical": false
    },
    {
      "edge_id": 101,
      "from_node": "23",
      "to_node": "71",
      "utilization_ratio": 0.05736636245110821,
      "congestion_score": 0.014341590612777053,
      "critical": false
    },
    {
      "edge_id": 30,
      "from_node": "24",
      "to_node": "26",
      "utilization_ratio": 0.06256242188445588,
      "congestion_score": 0.01564060547111397,
      "critical": false
    },
    {
      "edge_id": 34,
      "from_node": "25",
      "to_node": "29",
      "utilization_ratio": 0.004635665652614805,
      "congestion_score": 0.0011589164131537012,
      "critical": false
    },
    {
      "edge_id": 31,
      "from_node": "26",
      "to_node": "27",
      "utilization_ratio": 0.0447148582741803,
      "congestion_score": 0.011178714568545075,
      "critical": false
    },
    {
      "edge_id": 39,
      "from_node": "26",
      "to_node": "31",
      "utilization_ratio": 0.0871793617556331,
      "congestion_score": 0.021794840438908274,
      "critical": false
    },
    {
      "edge_id": 168,
      "from_node": "114",
      "to_node": "26",
      "utilization_ratio": 0.038505123250885925,
      "congestion_score": 0.009626280812721481,
      "critical": false
    },
    {
      "edge_id": 32,
      "from_node": "27",
      "to_node": "28",
      "utilization_ratio": 0.01902554444927326,
      "congestion_score": 0.004756386112318315,
      "critical": false
    },
    {
      "edge_id": 36,
      "from_node": "28",
      "to_node": "30",
      "utilization_ratio": 0.07465353228065091,
      "congestion_score": 0.01866338307016273,
      "critical": false
    },
    {
      "edge_id": 49,
      "from_node": "29",
      "to_node": "37",
      "utilization_ratio": 0.011589164131537013,
      "congestion_score": 0.0028972910328842532,
      "critical": false
    },
    {
      "edge_id": 38,
      "from_node": "30",
      "to_node": "31",
      "utilization_ratio": 0.24669153821696238,
      "congestion_score": 0.061672884554240595,
      "critical": false
    },
    {
      "edge_id": 166,
      "from_node": "112",
      "to_node": "31",
      "utilization_ratio": 0.2076746856407875,
      "congestion_score": 0.051918671410196876,
      "critical": false
    },
    {
      "edge_id": 167,
      "from_node": "113",
      "to_node": "31",
      "utilization_ratio": 0.0808632673039452,
      "congestion_score": 0.0202158168259863,
      "critical": false
    },
    {
      "edge_id": 44,
      "from_node": "32",
      "to_node": "36",
      "utilization_ratio": 0.43519104875037057,
      "congestion_score": 0.10879776218759264,
      "critical": false
    },
    {
      "edge_id": 45,
      "from_node": "33",
      "to_node": "35",
      "utilization_ratio": 0.04932155101646612,
      "congestion_score": 0.01233038775411653,
      "critical": false
    },
    {
      "edge_id": 46,
      "from_node": "33",
      "to_node": "36",
      "utilization_ratio": 0.08635375923511521,
      "congestion_score": 0.021588439808778802,
      "critical": false
    },
    {
      "edge_id": 55,
      "from_node": "33",
      "to_node": "42",
      "utilization_ratio": 0.1282161027923739,
      "congestion_score": 0.03205402569809347,
      "critical": false
    },
    {
      "edge_id": 42,
      "from_node": "34",
      "to_node": "35",
      "utilization_ratio": 0.016678738712637056,
      "congestion_score": 0.004169684678159264,
      "critical": false
    },
    {
      "edge_id": 43,
      "from_node": "34",
      "to_node": "36",
      "utilization_ratio": 0.07004683953836512,
      "congestion_score": 0.01751170988459128,
      "critical": false
    },
    {
      "edge_id": 47,
      "from_node": "36",
      "to_node": "38",
      "utilization_ratio": 0.021198512723936448,
      "congestion_score": 0.005299628180984112,
      "critical": false
    },
    {
      "edge_id": 48,
      "from_node": "36",
      "to_node": "39",
      "utilization_ratio": 0.547659057828549,
      "congestion_score": 0.13691476445713724,
      "critical": false
    },
    {
      "edge_id": 89,
      "from_node": "37",
      "to_node": "64",
      "utilization_ratio": 0.010430247718383311,
      "congestion_score": 0.002607561929595828,
      "critical": false
    },
    {
      "edge_id": 50,
      "from_node": "38",
      "to_node": "39",
      "utilization_ratio": 0.039065140760056016,
      "congestion_score": 0.009766285190014004,
      "critical": false
    },
    {
      "edge_id": 51,
      "from_node": "39",
      "to_node": "40",
      "utilization_ratio": 0.019646392527748458,
      "congestion_score": 0.0049115981319371145,
      "critical": false
    },
    {
      "edge_id": 52,
      "from_node": "39",
      "to_node": "41",
      "utilization_ratio": 0.5861999268778925,
      "congestion_score": 0.14654998171947312,
      "critical": false
    },
    {
      "edge_id": 53,
      "from_node": "40",
      "to_node": "41",
      "utilization_ratio": 0.040617260956244,
      "congestion_score": 0.010154315239061,
      "critical": false
    },
    {
      "edge_id": 62,
      "from_node": "41",
      "to_node": "48",
      "utilization_ratio": 0.6513475852458904,
      "congestion_score": 0.1628368963114726,
      "critical": false
    },
    {
      "edge_id": 54,
      "from_node": "42",
      "to_node": "43",
      "utilization_ratio": 0.14386147436994884,
      "congestion_score": 0.03596536859248721,
      "critical": false
    },
    {
      "edge_id": 56,
      "from_node": "43",
      "to_node": "44",
      "utilization_ratio": 0.16414953533597584,
      "congestion_score": 0.04103738383399396,
      "critical": false
    },
    {
      "edge_id": 57,
      "from_node": "44",
      "to_node": "45",
      "utilization_ratio": 0.02193249311893377,
      "congestion_score": 0.0054831232797334425,
      "critical": false
    },
    {
      "edge_id": 63,
      "from_node": "44",
      "to_node": "48",
      "utilization_ratio": 0.1801136089271683,
      "congestion_score": 0.045028402231792074,
      "critical": false
    },
    {
      "edge_id": 58,
      "from_node": "45",
      "to_node": "46",
      "utilization_ratio": 0.039036167849727146,
      "congestion_score": 0.009759041962431787,
      "critical": false
    },
    {
      "edge_id": 59,
      "from_node": "45",
      "to_node": "47",
      "utilization_ratio": 0.006924525568593359,
      "congestion_score": 0.0017311313921483397,
      "critical": false
    },
    {
      "edge_id": 60,
      "from_node": "46",
      "to_node": "48",
      "utilization_ratio": 0.028557631947462428,
      "congestion_score": 0.007139407986865607,
      "critical": false
    },
    {
      "edge_id": 96,
      "from_node": "46",
      "to_node": "68",
      "utilization_ratio": 0.06552706552706553,
      "congestion_score": 0.01638176638176638,
      "critical": false
    },
    {
      "edge_id": 64,
      "from_node": "47",
      "to_node": "48",
      "utilization_ratio": 0.06187647882563141,
      "congestion_score": 0.015469119706407852,
      "critical": false
    },
    {
      "edge_id": 65,
      "from_node": "48",
      "to_node": "49",
      "utilization_ratio": 0.11183543386933219,
      "congestion_score": 0.027958858467333047,
      "critical": false
    },
    {
      "edge_id": 66,
      "from_node": "48",
      "to_node": "50",
      "utilization_ratio": 0.16514558887440242,
      "congestion_score": 0.041286397218600605,
      "critical": false
    },
    {
      "edge_id": 71,
      "from_node": "48",
      "to_node": "53",
      "utilization_ratio": 0.32101984644357523,
      "congestion_score": 0.08025496161089381,
      "critical": false
    },
    {
      "edge_id": 92,
      "from_node": "48",
      "to_node": "65",
      "utilization_ratio": 0.22173934038340817,
      "congestion_score": 0.05543483509585204,
      "critical": false
    },
    {
      "edge_id": 97,
      "from_node": "48",
      "to_node": "68",
      "utilization_ratio": 1.0,
      "congestion_score": 0.2642948702270739,
      "critical": true
    },
    {
      "edge_id": 76,
      "from_node": "49",
      "to_node": "56",
      "utilization_ratio": 0.05640059877348014,
      "congestion_score": 0.014100149693370034,
      "critical": false
    },
    {
      "edge_id": 67,
      "from_node": "50",
      "to_node": "51",
      "utilization_ratio": 0.057173209715582596,
      "congestion_score": 0.014293302428895649,
      "critical": false
    },
    {
      "edge_id": 78,
      "from_node": "50",
      "to_node": "57",
      "utilization_ratio": 0.05755951518663384,
      "congestion_score": 0.01438987879665846,
      "critical": false
    },
    {
      "edge_id": 68,
      "from_node": "51",
      "to_node": "52",
      "utilization_ratio": 0.004828818388140421,
      "congestion_score": 0.0012072045970351053,
      "critical": false
    },
    {
      "edge_id": 69,
      "from_node": "52",
      "to_node": "53",
      "utilization_ratio": 0.06219518083924864,
      "congestion_score": 0.01554879520981216,
      "critical": false
    },
    {
      "edge_id": 72,
      "from_node": "53",
      "to_node": "54",
      "utilization_ratio": 0.05524168236032643,
      "congestion_score": 0.013810420590081607,
      "critical": false
    },
    {
      "edge_id": 73,
      "from_node": "53",
      "to_node": "55",
      "utilization_ratio": 0.05659375150900575,
      "congestion_score": 0.014148437877251438,
      "critical": false
    },
    {
      "edge_id": 79,
      "from_node": "53",
      "to_node": "58",
      "utilization_ratio": 0.11183543386933216,
      "congestion_score": 0.02795885846733304,
      "critical": false
    },
    {
      "edge_id": 74,
      "from_node": "54",
      "to_node": "55",
      "utilization_ratio": 0.0023178328263074024,
      "congestion_score": 0.0005794582065768506,
      "critical": false
    },
    {
      "edge_id": 82,
      "from_node": "54",
      "to_node": "58",
      "utilization_ratio": 0.002704138297358636,
      "congestion_score": 0.000676034574339659,
      "critical": false
    },
    {
      "edge_id": 75,
      "from_node": "55",
      "to_node": "56",
      "utilization_ratio": 0.007532956685499057,
      "congestion_score": 0.0018832391713747643,
      "critical": false
    },
    {
      "edge_id": 77,
      "from_node": "55",
      "to_node": "57",
      "utilization_ratio": 0.007339803949973441,
      "congestion_score": 0.0018349509874933602,
      "critical": false
    },
    {
      "edge_id": 81,
      "from_node": "55",
      "to_node": "58",
      "utilization_ratio": 0.008305567627601526,
      "congestion_score": 0.0020763919069003815,
      "critical": false
    },
    {
      "edge_id": 83,
      "from_node": "58",
      "to_node": "59",
      "utilization_ratio": 0.03399488145250857,
      "congestion_score": 0.008498720363127142,
      "critical": false
    },
    {
      "edge_id": 84,
      "from_node": "58",
      "to_node": "60",
      "utilization_ratio": 0.03399488145250857,
      "congestion_score": 0.008498720363127142,
      "critical": false
    },
    {
      "edge_id": 85,
      "from_node": "59",
      "to_node": "60",
      "utilization_ratio": 0.0005794582065768506,
      "congestion_score": 0.00014486455164421265,
      "critical": false
    },
    {
      "edge_id": 86,
      "from_node": "59",
      "to_node": "61",
      "utilization_ratio": 0.03071128494857308,
      "congestion_score": 0.00767782123714327,
      "critical": false
    },
    {
      "edge_id": 87,
      "from_node": "60",
      "to_node": "61",
      "utilization_ratio": 0.03071128494857308,
      "congestion_score": 0.00767782123714327,
      "critical": false
    },
    {
      "edge_id": 93,
      "from_node": "61",
      "to_node": "65",
      "utilization_ratio": 0.1097107537785504,
      "congestion_score": 0.0274276884446376,
      "critical": false
    },
    {
      "edge_id": 94,
      "from_node": "61",
      "to_node": "66",
      "utilization_ratio": 0.0030904437684098696,
      "congestion_score": 0.0007726109421024674,
      "critical": false
    },
    {
      "edge_id": 88,
      "from_node": "62",
      "to_node": "63",
      "utilization_ratio": 0.004635665652614805,
      "congestion_score": 0.0011589164131537012,
      "critical": false
    },
    {
      "edge_id": 90,
      "from_node": "63",
      "to_node": "64",
      "utilization_ratio": 0.008112414892075908,
      "congestion_score": 0.002028103723018977,
      "critical": false
    },
    {
      "edge_id": 95,
      "from_node": "65",
      "to_node": "66",
      "utilization_ratio": 0.05717320971558259,
      "congestion_score": 0.014293302428895647,
      "critical": false
    },
    {
      "edge_id": 98,
      "from_node": "68",
      "to_node": "69",
      "utilization_ratio": 0.5205942833061469,
      "congestion_score": 0.13014857082653672,
      "critical": false
    },
    {
      "edge_id": 106,
      "from_node": "68",
      "to_node": "74",
      "utilization_ratio": 0.048917309934259086,
      "congestion_score": 0.012229327483564771,
      "critical": false
    },
    {
      "edge_id": 109,
      "from_node": "68",
      "to_node": "76",
      "utilization_ratio": 1.0,
      "congestion_score": 0.27277581175886273,
      "critical": true
    },
    {
      "edge_id": 100,
      "from_node": "69",
      "to_node": "70",
      "utilization_ratio": 0.11994784876140807,
      "congestion_score": 0.029986962190352018,
      "critical": false
    },
    {
      "edge_id": 104,
      "from_node": "69",
      "to_node": "73",
      "utilization_ratio": 0.02955236853541938,
      "congestion_score": 0.007388092133854845,
      "critical": false
    },
    {
      "edge_id": 105,
      "from_node": "69",
      "to_node": "74",
      "utilization_ratio": 0.30572766843953336,
      "congestion_score": 0.07643191710988334,
      "critical": false
    },
    {
      "edge_id": 102,
      "from_node": "70",
      "to_node": "71",
      "utilization_ratio": 0.03882369984064899,
      "congestion_score": 0.009705924960162248,
      "critical": false
    },
    {
      "edge_id": 103,
      "from_node": "70",
      "to_node": "72",
      "utilization_ratio": 0.060263653483992465,
      "congestion_score": 0.015065913370998116,
      "critical": false
    },
    {
      "edge_id": 107,
      "from_node": "73",
      "to_node": "74",
      "utilization_ratio": 0.030711284948573083,
      "congestion_score": 0.007677821237143271,
      "critical": false
    },
    {
      "edge_id": 110,
      "from_node": "74",
      "to_node": "76",
      "utilization_ratio": 0.31241351241351284,
      "congestion_score": 0.07810337810337821,
      "critical": false
    },
    {
      "edge_id": 171,
      "from_node": "117",
      "to_node": "74",
      "utilization_ratio": 0.05555900471154707,
      "congestion_score": 0.013889751177886768,
      "critical": false
    },
    {
      "edge_id": 108,
      "from_node": "75",
      "to_node": "76",
      "utilization_ratio": 0.06380938584328413,
      "congestion_score": 0.015952346460821033,
      "critical": false
    },
    {
      "edge_id": 172,
      "from_node": "117",
      "to_node": "75",
      "utilization_ratio": 0.016155846664321242,
      "congestion_score": 0.0040389616660803105,
      "critical": false
    },
    {
      "edge_id": 111,
      "from_node": "76",
      "to_node": "77",
      "utilization_ratio": 0.07543868560817714,
      "congestion_score": 0.018859671402044285,
      "critical": false
    },
    {
      "edge_id": 114,
      "from_node": "76",
      "to_node": "79",
      "utilization_ratio": 0.879527754104025,
      "congestion_score": 0.21988193852600624,
      "critical": true
    },
    {
      "edge_id": 116,
      "from_node": "76",
      "to_node": "81",
      "utilization_ratio": 0.4558848558848557,
      "congestion_score": 0.11397121397121393,
      "critical": false
    },
    {
      "edge_id": 112,
      "from_node": "77",
      "to_node": "78",
      "utilization_ratio": 0.028670638840130356,
      "congestion_score": 0.007167659710032589,
      "critical": false
    },
    {
      "edge_id": 115,
      "from_node": "78",
      "to_node": "79",
      "utilization_ratio": 0.043929704946654095,
      "congestion_score": 0.010982426236663524,
      "critical": false
    },
    {
      "edge_id": 135,
      "from_node": "79",
      "to_node": "95",
      "utilization_ratio": 0.12577328509531902,
      "congestion_score": 0.031443321273829754,
      "critical": false
    },
    {
      "edge_id": 138,
      "from_node": "79",
      "to_node": "96",
      "utilization_ratio": 0.04925394755903227,
      "congestion_score": 0.012313486889758068,
      "critical": false
    },
    {
      "edge_id": 139,
      "from_node": "79",
      "to_node": "97",
      "utilization_ratio": 0.34734756768655045,
      "congestion_score": 0.08683689192163761,
      "critical": false
    },
    {
      "edge_id": 140,
      "from_node": "79",
      "to_node": "98",
      "utilization_ratio": 0.34734756768655045,
      "congestion_score": 0.08683689192163761,
      "critical": false
    },
    {
      "edge_id": 117,
      "from_node": "81",
      "to_node": "82",
      "utilization_ratio": 0.318740644164373,
      "congestion_score": 0.07968516104109324,
      "critical": false
    },
    {
      "edge_id": 136,
      "from_node": "81",
      "to_node": "95",
      "utilization_ratio": 0.13950067509389538,
      "congestion_score": 0.034875168773473846,
      "critical": false
    },
    {
      "edge_id": 118,
      "from_node": "82",
      "to_node": "83",
      "utilization_ratio": 0.04741899657153894,
      "congestion_score": 0.011854749142884735,
      "critical": false
    },
    {
      "edge_id": 119,
      "from_node": "82",
      "to_node": "84",
      "utilization_ratio": 0.22921435124824951,
      "congestion_score": 0.05730358781206238,
      "critical": false
    },
    {
      "edge_id": 120,
      "from_node": "83",
      "to_node": "84",
      "utilization_ratio": 0.01284465691245352,
      "congestion_score": 0.00321116422811338,
      "critical": false
    },
    {
      "edge_id": 121,
      "from_node": "84",
      "to_node": "85",
      "utilization_ratio": 0.060263653483992465,
      "congestion_score": 0.015065913370998116,
      "critical": false
    },
    {
      "edge_id": 122,
      "from_node": "84",
      "to_node": "87",
      "utilization_ratio": 0.04629871070549037,
      "congestion_score": 0.011574677676372592,
      "critical": false
    },
    {
      "edge_id": 123,
      "from_node": "84",
      "to_node": "88",
      "utilization_ratio": 0.128543145492298,
      "congestion_score": 0.0321357863730745,
      "critical": false
    },
    {
      "edge_id": 124,
      "from_node": "87",
      "to_node": "88",
      "utilization_ratio": 0.0139649427785021,
      "congestion_score": 0.003491235694625525,
      "critical": false
    },
    {
      "edge_id": 126,
      "from_node": "88",
      "to_node": "89",
      "utilization_ratio": 0.054758800521512385,
      "congestion_score": 0.013689700130378096,
      "critical": false
    },
    {
      "edge_id": 129,
      "from_node": "88",
      "to_node": "91",
      "utilization_ratio": 0.06978608334540537,
      "congestion_score": 0.017446520836351342,
      "critical": false
    },
    {
      "edge_id": 127,
      "from_node": "89",
      "to_node": "90",
      "utilization_ratio": 0.008981602201941184,
      "congestion_score": 0.002245400550485296,
      "critical": false
    },
    {
      "edge_id": 130,
      "from_node": "90",
      "to_node": "91",
      "utilization_ratio": 0.06460959003331884,
      "congestion_score": 0.01615239750832971,
      "critical": false
    },
    {
      "edge_id": 131,
      "from_node": "91",
      "to_node": "92",
      "utilization_ratio": 0.009657636776280842,
      "congestion_score": 0.0024144091940702106,
      "critical": false
    },
    {
      "edge_id": 132,
      "from_node": "91",
      "to_node": "93",
      "utilization_ratio": 0.07536619062042788,
      "congestion_score": 0.01884154765510697,
      "critical": false
    },
    {
      "edge_id": 141,
      "from_node": "91",
      "to_node": "99",
      "utilization_ratio": 0.13339504186961812,
      "congestion_score": 0.03334876046740453,
      "critical": false
    },
    {
      "edge_id": 148,
      "from_node": "101",
      "to_node": "91",
      "utilization_ratio": 0.04404057963379996,
      "congestion_score": 0.01101014490844999,
      "critical": false
    },
    {
      "edge_id": 133,
      "from_node": "92",
      "to_node": "93",
      "utilization_ratio": 0.050606016707711615,
      "congestion_score": 0.012651504176927904,
      "critical": false
    },
    {
      "edge_id": 134,
      "from_node": "93",
      "to_node": "94",
      "utilization_ratio": 0.012748080544690713,
      "congestion_score": 0.003187020136172678,
      "critical": false
    },
    {
      "edge_id": 137,
      "from_node": "93",
      "to_node": "95",
      "utilization_ratio": 0.17754398771347946,
      "congestion_score": 0.044385996928369864,
      "critical": false
    },
    {
      "edge_id": 142,
      "from_node": "93",
      "to_node": "99",
      "utilization_ratio": 0.03921000531170021,
      "congestion_score": 0.009802501327925053,
      "critical": false
    },
    {
      "edge_id": 143,
      "from_node": "94",
      "to_node": "95",
      "utilization_ratio": 0.047515572939301746,
      "congestion_score": 0.011878893234825437,
      "critical": false
    },
    {
      "edge_id": 144,
      "from_node": "95",
      "to_node": "96",
      "utilization_ratio": 0.011009705924960169,
      "congestion_score": 0.0027524264812400423,
      "critical": false
    },
    {
      "edge_id": 145,
      "from_node": "97",
      "to_node": "99",
      "utilization_ratio": 0.3141252971761445,
      "congestion_score": 0.07853132429403613,
      "critical": false
    },
    {
      "edge_id": 146,
      "from_node": "98",
      "to_node": "99",
      "utilization_ratio": 0.3141252971761445,
      "congestion_score": 0.07853132429403613,
      "critical": false
    },
    {
      "edge_id": 147,
      "from_node": "100",
      "to_node": "99",
      "utilization_ratio": 0.07532781092103125,
      "congestion_score": 0.01883195273025781,
      "critical": false
    },
    {
      "edge_id": 150,
      "from_node": "102",
      "to_node": "99",
      "utilization_ratio": 0.31310058428702525,
      "congestion_score": 0.07827514607175631,
      "critical": false
    },
    {
      "edge_id": 151,
      "from_node": "103",
      "to_node": "99",
      "utilization_ratio": 0.09203727847795648,
      "congestion_score": 0.02300931961948912,
      "critical": false
    },
    {
      "edge_id": 154,
      "from_node": "105",
      "to_node": "99",
      "utilization_ratio": 0.1482447245159109,
      "congestion_score": 0.03706118112897772,
      "critical": false
    },
    {
      "edge_id": 149,
      "from_node": "100",
      "to_node": "101",
      "utilization_ratio": 0.021631350444909752,
      "congestion_score": 0.005407837611227438,
      "critical": false
    },
    {
      "edge_id": 152,
      "from_node": "102",
      "to_node": "103",
      "utilization_ratio": 0.002607561929595828,
      "congestion_score": 0.000651890482398957,
      "critical": false
    },
    {
      "edge_id": 153,
      "from_node": "102",
      "to_node": "104",
      "utilization_ratio": 0.04307306002221253,
      "congestion_score": 0.010768265005553132,
      "critical": false
    },
    {
      "edge_id": 161,
      "from_node": "102",
      "to_node": "109",
      "utilization_ratio": 0.22975517890772126,
      "congestion_score": 0.057438794726930316,
      "critical": false
    },
    {
      "edge_id": 155,
      "from_node": "103",
      "to_node": "104",
      "utilization_ratio": 0.03901685257617457,
      "congestion_score": 0.009754213144043643,
      "critical": false
    },
    {
      "edge_id": 156,
      "from_node": "104",
      "to_node": "105",
      "utilization_ratio": 0.03988603988603985,
      "congestion_score": 0.009971509971509963,
      "critical": false
    },
    {
      "edge_id": 157,
      "from_node": "104",
      "to_node": "106",
      "utilization_ratio": 0.004635665652614805,
      "congestion_score": 0.0011589164131537012,
      "critical": false
    },
    {
      "edge_id": 158,
      "from_node": "104",
      "to_node": "107",
      "utilization_ratio": 0.059973924380704036,
      "congestion_score": 0.014993481095176009,
      "critical": false
    },
    {
      "edge_id": 159,
      "from_node": "105",
      "to_node": "106",
      "utilization_ratio": 0.05562798783137766,
      "congestion_score": 0.013906996957844414,
      "critical": false
    },
    {
      "edge_id": 160,
      "from_node": "107",
      "to_node": "108",
      "utilization_ratio": 0.004345936549326379,
      "congestion_score": 0.0010864841373315949,
      "critical": false
    },
    {
      "edge_id": 162,
      "from_node": "108",
      "to_node": "109",
      "utilization_ratio": 0.059394466174127185,
      "congestion_score": 0.014848616543531796,
      "critical": false
    },
    {
      "edge_id": 163,
      "from_node": "109",
      "to_node": "110",
      "utilization_ratio": 0.060263653483992465,
      "congestion_score": 0.015065913370998116,
      "critical": false
    },
    {
      "edge_id": 164,
      "from_node": "109",
      "to_node": "111",
      "utilization_ratio": 0.060263653483992465,
      "congestion_score": 0.015065913370998116,
      "critical": false
    },
    {
      "edge_id": 169,
      "from_node": "113",
      "to_node": "114",
      "utilization_ratio": 0.023303752117311435,
      "congestion_score": 0.005825938029327859,
      "critical": false
    }
  ],
  "hotspots": [
    {
      "hotspot_id": "primary_hotspot",
      "affected_edges": [
        97,
        109,
        114
      ],
      "average_congestion_score": 0.2523175401706476,
      "severity_level": "MODERATE"
    }
  ],
  "network_stress_metrics": {
    "average_network_stress": 0.12858422331569155,
    "max_network_stress": 1.0,
    "num_critical_edges": 3,
    "congestion_distribution_score": 0.018072289156626505
  },
  "expansion_relief_impacts": [
    {
      "candidate_id": "cand_parallel_14_16_cap11880_c414_hae0123",
      "relief_score": 2868276.137334061,
      "estimated_stress_reduction": 1.0,
      "strategic_importance": 0.0
    },
    {
      "candidate_id": "cand_parallel_22_24_cap11880_c414_hef94ba",
      "relief_score": 2868276.137334061,
      "estimated_stress_reduction": 1.0,
      "strategic_importance": 0.0
    },
    {
      "candidate_id": "cand_parallel_24_26_cap11880_c414_haaf7f6",
      "relief_score": 2868276.137334061,
      "estimated_stress_reduction": 1.0,
      "strategic_importance": 0.0
    },
    {
      "candidate_id": "cand_parallel_25_29_cap11880_c331_h41b49c",
      "relief_score": 3585345.1716675754,
      "estimated_stress_reduction": 1.0,
      "strategic_importance": 1.0
    },
    {
      "candidate_id": "cand_parallel_33_36_cap11880_c414_h980a6c",
      "relief_score": 2868276.137334061,
      "estimated_stress_reduction": 1.0,
      "strategic_importance": 0.0
    },
    {
      "candidate_id": "cand_parallel_37_64_cap11880_c331_h356a82",
      "relief_score": 3585345.1716675754,
      "estimated_stress_reduction": 1.0,
      "strategic_importance": 1.0
    },
    {
      "candidate_id": "cand_parallel_3_4_cap11880_c414_hf4ebbf",
      "relief_score": 2868276.137334061,
      "estimated_stress_reduction": 1.0,
      "strategic_importance": 0.0
    },
    {
      "candidate_id": "cand_parallel_48_65_cap11880_c414_v0_h534daa",
      "relief_score": 2868276.137334061,
      "estimated_stress_reduction": 1.0,
      "strategic_importance": 0.0
    },
    {
      "candidate_id": "cand_parallel_48_65_cap11880_c414_v1_h534daa",
      "relief_score": 2868276.137334061,
      "estimated_stress_reduction": 1.0,
      "strategic_importance": 0.0
    },
    {
      "candidate_id": "cand_parallel_59_60_cap11880_c414_h20e9d5",
      "relief_score": 2868276.137334061,
      "estimated_stress_reduction": 1.0,
      "strategic_importance": 0.0
    },
    {
      "candidate_id": "cand_parallel_62_63_cap11880_c331_h692783",
      "relief_score": 3585345.1716675754,
      "estimated_stress_reduction": 1.0,
      "strategic_importance": 1.0
    },
    {
      "candidate_id": "cand_parallel_63_64_cap11880_c331_ha047ae",
      "relief_score": 3585345.1716675754,
      "estimated_stress_reduction": 1.0,
      "strategic_importance": 1.0
    },
    {
      "candidate_id": "cand_parallel_68_69_cap11880_c414_hf83bb2",
      "relief_score": 2868276.137334061,
      "estimated_stress_reduction": 1.0,
      "strategic_importance": 0.0
    },
    {
      "candidate_id": "cand_parallel_68_74_cap11880_c414_h8959b7",
      "relief_score": 2868276.137334061,
      "estimated_stress_reduction": 1.0,
      "strategic_importance": 0.0
    },
    {
      "candidate_id": "cand_parallel_76_79_cap11880_c414_h27c6d6",
      "relief_score": 2868276.137334061,
      "estimated_stress_reduction": 1.0,
      "strategic_importance": 0.0
    },
    {
      "candidate_id": "cand_parallel_7_29_cap11880_c331_h36c98e",
      "relief_score": 3585345.1716675754,
      "estimated_stress_reduction": 1.0,
      "strategic_importance": 1.0
    },
    {
      "candidate_id": "cand_parallel_7_8_cap11880_c331_h8974c8",
      "relief_score": 3585345.1716675754,
      "estimated_stress_reduction": 1.0,
      "strategic_importance": 1.0
    },
    {
      "candidate_id": "cand_parallel_87_88_cap11880_c414_h5ce888",
      "relief_score": 2868276.137334061,
      "estimated_stress_reduction": 1.0,
      "strategic_importance": 0.0
    },
    {
      "candidate_id": "cand_parallel_88_89_cap11880_c414_h1a4b7e",
      "relief_score": 2868276.137334061,
      "estimated_stress_reduction": 1.0,
      "strategic_importance": 0.0
    },
    {
      "candidate_id": "cand_parallel_88_91_cap11880_c414_h105318",
      "relief_score": 2868276.137334061,
      "estimated_stress_reduction": 1.0,
      "strategic_importance": 0.0
    },
    {
      "candidate_id": "cand_parallel_8_9_cap11880_c331_hbce51e",
      "relief_score": 3585345.1716675754,
      "estimated_stress_reduction": 1.0,
      "strategic_importance": 1.0
    },
    {
      "candidate_id": "cand_parallel_99_102_cap11880_c414_h2e3cee",
      "relief_score": 2868276.137334061,
      "estimated_stress_reduction": 1.0,
      "strategic_importance": 0.0
    }
  ]
}

## Resilience
{
  "critical_edges": [
    {
      "edge_id": 40,
      "from_node": "14",
      "to_node": "32",
      "bridge_edge": false,
      "edge_betweenness": 0.10300318012182413,
      "criticality_score": 0.10300318012182413
    },
    {
      "edge_id": 28,
      "from_node": "22",
      "to_node": "23",
      "bridge_edge": false,
      "edge_betweenness": 0.1820983787085483,
      "criticality_score": 0.1820983787085483
    },
    {
      "edge_id": 37,
      "from_node": "22",
      "to_node": "31",
      "bridge_edge": false,
      "edge_betweenness": 0.1319027488519012,
      "criticality_score": 0.1319027488519012
    },
    {
      "edge_id": 99,
      "from_node": "23",
      "to_node": "69",
      "bridge_edge": false,
      "edge_betweenness": 0.18311243057005777,
      "criticality_score": 0.18311243057005777
    },
    {
      "edge_id": 44,
      "from_node": "32",
      "to_node": "36",
      "bridge_edge": false,
      "edge_betweenness": 0.10879776218759264,
      "criticality_score": 0.10879776218759264
    },
    {
      "edge_id": 48,
      "from_node": "36",
      "to_node": "39",
      "bridge_edge": false,
      "edge_betweenness": 0.13691476445713724,
      "criticality_score": 0.13691476445713724
    },
    {
      "edge_id": 52,
      "from_node": "39",
      "to_node": "41",
      "bridge_edge": false,
      "edge_betweenness": 0.14654998171947312,
      "criticality_score": 0.14654998171947312
    },
    {
      "edge_id": 62,
      "from_node": "41",
      "to_node": "48",
      "bridge_edge": false,
      "edge_betweenness": 0.1628368963114726,
      "criticality_score": 0.1628368963114726
    },
    {
      "edge_id": 97,
      "from_node": "48",
      "to_node": "68",
      "bridge_edge": false,
      "edge_betweenness": 0.2642948702270739,
      "criticality_score": 0.2642948702270739
    },
    {
      "edge_id": 98,
      "from_node": "68",
      "to_node": "69",
      "bridge_edge": false,
      "edge_betweenness": 0.13014857082653672,
      "criticality_score": 0.13014857082653672
    },
    {
      "edge_id": 109,
      "from_node": "68",
      "to_node": "76",
      "bridge_edge": false,
      "edge_betweenness": 0.27277581175886273,
      "criticality_score": 0.27277581175886273
    },
    {
      "edge_id": 114,
      "from_node": "76",
      "to_node": "79",
      "bridge_edge": false,
      "edge_betweenness": 0.21988193852600624,
      "criticality_score": 0.21988193852600624
    },
    {
      "edge_id": 116,
      "from_node": "76",
      "to_node": "81",
      "bridge_edge": false,
      "edge_betweenness": 0.11397121397121393,
      "criticality_score": 0.11397121397121393
    }
  ],
  "vulnerabilities": [
    {
      "vulnerability_id": "vulnerability_48",
      "affected_nodes": [
        "48"
      ],
      "affected_edges": [
        "48_41",
        "48_44",
        "48_46",
        "48_47",
        "48_49",
        "48_50",
        "48_53",
        "48_65",
        "48_68"
      ],
      "fragmentation_risk": 0.9,
      "severity_level": "HIGH"
    },
    {
      "vulnerability_id": "vulnerability_84",
      "affected_nodes": [
        "84"
      ],
      "affected_edges": [
        "84_82",
        "84_83",
        "84_85",
        "84_87",
        "84_88"
      ],
      "fragmentation_risk": 0.5,
      "severity_level": "HIGH"
    },
    {
      "vulnerability_id": "vulnerability_109",
      "affected_nodes": [
        "109"
      ],
      "affected_edges": [
        "109_102",
        "109_108",
        "109_110",
        "109_111"
      ],
      "fragmentation_risk": 0.4,
      "severity_level": "MODERATE"
    },
    {
      "vulnerability_id": "vulnerability_99",
      "affected_nodes": [
        "99"
      ],
      "affected_edges": [
        "99_91",
        "99_93",
        "99_97",
        "99_98",
        "99_100",
        "99_102",
        "99_103",
        "99_105"
      ],
      "fragmentation_risk": 0.8,
      "severity_level": "HIGH"
    },
    {
      "vulnerability_id": "vulnerability_76",
      "affected_nodes": [
        "76"
      ],
      "affected_edges": [
        "76_68",
        "76_74",
        "76_75",
        "76_77",
        "76_79",
        "76_81"
      ],
      "fragmentation_risk": 0.6,
      "severity_level": "HIGH"
    },
    {
      "vulnerability_id": "vulnerability_70",
      "affected_nodes": [
        "70"
      ],
      "affected_edges": [
        "70_69",
        "70_71",
        "70_72"
      ],
      "fragmentation_risk": 0.3,
      "severity_level": "MODERATE"
    },
    {
      "vulnerability_id": "vulnerability_11",
      "affected_nodes": [
        "11"
      ],
      "affected_edges": [
        "11_1",
        "11_2",
        "11_6",
        "11_10",
        "11_13",
        "11_15",
        "11_116"
      ],
      "fragmentation_risk": 0.7,
      "severity_level": "HIGH"
    },
    {
      "vulnerability_id": "vulnerability_8",
      "affected_nodes": [
        "8"
      ],
      "affected_edges": [
        "8_7",
        "8_9"
      ],
      "fragmentation_risk": 0.2,
      "severity_level": "MODERATE"
    },
    {
      "vulnerability_id": "vulnerability_29",
      "affected_nodes": [
        "29"
      ],
      "affected_edges": [
        "29_7",
        "29_25",
        "29_37"
      ],
      "fragmentation_risk": 0.3,
      "severity_level": "MODERATE"
    },
    {
      "vulnerability_id": "vulnerability_63",
      "affected_nodes": [
        "63"
      ],
      "affected_edges": [
        "63_62",
        "63_64"
      ],
      "fragmentation_risk": 0.2,
      "severity_level": "MODERATE"
    },
    {
      "vulnerability_id": "vulnerability_64",
      "affected_nodes": [
        "64"
      ],
      "affected_edges": [
        "64_37",
        "64_63"
      ],
      "fragmentation_risk": 0.2,
      "severity_level": "MODERATE"
    },
    {
      "vulnerability_id": "vulnerability_37",
      "affected_nodes": [
        "37"
      ],
      "affected_edges": [
        "37_29",
        "37_64"
      ],
      "fragmentation_risk": 0.2,
      "severity_level": "MODERATE"
    },
    {
      "vulnerability_id": "vulnerability_7",
      "affected_nodes": [
        "7"
      ],
      "affected_edges": [
        "7_8",
        "7_29"
      ],
      "fragmentation_risk": 0.2,
      "severity_level": "MODERATE"
    }
  ],
  "resilience_metrics": {
    "network_connectivity_score": 0.0,
    "redundancy_score": 0.024047515572939302,
    "resilience_score": 0.012023757786469651,
    "num_critical_edges": 13,
    "num_articulation_points": 13
  },
  "expansion_impacts": [
    {
      "candidate_id": "cand_parallel_14_16_cap11880_c414_hae0123",
      "resilience_gain_score": 0.0,
      "redundancy_improvement": 1.0,
      "survivability_contribution": 0.0
    },
    {
      "candidate_id": "cand_parallel_22_24_cap11880_c414_hef94ba",
      "resilience_gain_score": 0.0,
      "redundancy_improvement": 1.0,
      "survivability_contribution": 0.0
    },
    {
      "candidate_id": "cand_parallel_24_26_cap11880_c414_haaf7f6",
      "resilience_gain_score": 0.0,
      "redundancy_improvement": 1.0,
      "survivability_contribution": 0.0
    },
    {
      "candidate_id": "cand_parallel_25_29_cap11880_c331_h41b49c",
      "resilience_gain_score": 1.0,
      "redundancy_improvement": 1.0,
      "survivability_contribution": 1.25
    },
    {
      "candidate_id": "cand_parallel_33_36_cap11880_c414_h980a6c",
      "resilience_gain_score": 0.0,
      "redundancy_improvement": 1.0,
      "survivability_contribution": 0.0
    },
    {
      "candidate_id": "cand_parallel_37_64_cap11880_c331_h356a82",
      "resilience_gain_score": 1.0,
      "redundancy_improvement": 1.0,
      "survivability_contribution": 1.25
    },
    {
      "candidate_id": "cand_parallel_3_4_cap11880_c414_hf4ebbf",
      "resilience_gain_score": 0.0,
      "redundancy_improvement": 1.0,
      "survivability_contribution": 0.0
    },
    {
      "candidate_id": "cand_parallel_48_65_cap11880_c414_v0_h534daa",
      "resilience_gain_score": 0.0,
      "redundancy_improvement": 1.0,
      "survivability_contribution": 0.0
    },
    {
      "candidate_id": "cand_parallel_48_65_cap11880_c414_v1_h534daa",
      "resilience_gain_score": 0.0,
      "redundancy_improvement": 1.0,
      "survivability_contribution": 0.0
    },
    {
      "candidate_id": "cand_parallel_59_60_cap11880_c414_h20e9d5",
      "resilience_gain_score": 0.0,
      "redundancy_improvement": 1.0,
      "survivability_contribution": 0.0
    },
    {
      "candidate_id": "cand_parallel_62_63_cap11880_c331_h692783",
      "resilience_gain_score": 1.0,
      "redundancy_improvement": 1.0,
      "survivability_contribution": 1.25
    },
    {
      "candidate_id": "cand_parallel_63_64_cap11880_c331_ha047ae",
      "resilience_gain_score": 1.0,
      "redundancy_improvement": 1.0,
      "survivability_contribution": 1.25
    },
    {
      "candidate_id": "cand_parallel_68_69_cap11880_c414_hf83bb2",
      "resilience_gain_score": 0.0,
      "redundancy_improvement": 1.0,
      "survivability_contribution": 0.0
    },
    {
      "candidate_id": "cand_parallel_68_74_cap11880_c414_h8959b7",
      "resilience_gain_score": 0.0,
      "redundancy_improvement": 1.0,
      "survivability_contribution": 0.0
    },
    {
      "candidate_id": "cand_parallel_76_79_cap11880_c414_h27c6d6",
      "resilience_gain_score": 0.0,
      "redundancy_improvement": 1.0,
      "survivability_contribution": 0.0
    },
    {
      "candidate_id": "cand_parallel_7_29_cap11880_c331_h36c98e",
      "resilience_gain_score": 1.0,
      "redundancy_improvement": 1.0,
      "survivability_contribution": 1.25
    },
    {
      "candidate_id": "cand_parallel_7_8_cap11880_c331_h8974c8",
      "resilience_gain_score": 1.0,
      "redundancy_improvement": 1.0,
      "survivability_contribution": 1.25
    },
    {
      "candidate_id": "cand_parallel_87_88_cap11880_c414_h5ce888",
      "resilience_gain_score": 0.0,
      "redundancy_improvement": 1.0,
      "survivability_contribution": 0.0
    },
    {
      "candidate_id": "cand_parallel_88_89_cap11880_c414_h1a4b7e",
      "resilience_gain_score": 0.0,
      "redundancy_improvement": 1.0,
      "survivability_contribution": 0.0
    },
    {
      "candidate_id": "cand_parallel_88_91_cap11880_c414_h105318",
      "resilience_gain_score": 0.0,
      "redundancy_improvement": 1.0,
      "survivability_contribution": 0.0
    },
    {
      "candidate_id": "cand_parallel_8_9_cap11880_c331_hbce51e",
      "resilience_gain_score": 1.0,
      "redundancy_improvement": 1.0,
      "survivability_contribution": 1.25
    },
    {
      "candidate_id": "cand_parallel_99_102_cap11880_c414_h2e3cee",
      "resilience_gain_score": 0.0,
      "redundancy_improvement": 1.0,
      "survivability_contribution": 0.0
    }
  ]
}

## Reasoning
{
  "expansion_explanations": [
    {
      "candidate_id": "cand_parallel_14_16_cap11880_c414_hae0123",
      "explanation": "Expansion candidate cand_parallel_14_16_cap11880_c414_hae0123 was selected to improve network reinforcement capacity between 14 and 16. The expansion contributes 11880.0 MVA of additional transmission capacity with a strategic decision score of 0.00. This reinforcement supports topology robustness and congestion relief objectives while maintaining infrastructure investment efficiency.",
      "reinforcement_priority": "MODERATE",
      "strategic_importance": 0.0
    },
    {
      "candidate_id": "cand_parallel_22_24_cap11880_c414_hef94ba",
      "explanation": "Expansion candidate cand_parallel_22_24_cap11880_c414_hef94ba was selected to improve network reinforcement capacity between 22 and 24. The expansion contributes 11880.0 MVA of additional transmission capacity with a strategic decision score of 0.00. This reinforcement supports topology robustness and congestion relief objectives while maintaining infrastructure investment efficiency.",
      "reinforcement_priority": "MODERATE",
      "strategic_importance": 0.0
    },
    {
      "candidate_id": "cand_parallel_24_26_cap11880_c414_haaf7f6",
      "explanation": "Expansion candidate cand_parallel_24_26_cap11880_c414_haaf7f6 was selected to improve network reinforcement capacity between 24 and 26. The expansion contributes 11880.0 MVA of additional transmission capacity with a strategic decision score of 0.00. This reinforcement supports topology robustness and congestion relief objectives while maintaining infrastructure investment efficiency.",
      "reinforcement_priority": "MODERATE",
      "strategic_importance": 0.0
    },
    {
      "candidate_id": "cand_parallel_25_29_cap11880_c331_h41b49c",
      "explanation": "Expansion candidate cand_parallel_25_29_cap11880_c331_h41b49c was selected to improve network reinforcement capacity between 25 and 29. The expansion contributes 11880.0 MVA of additional transmission capacity with a strategic decision score of 1.00. This reinforcement supports topology robustness and congestion relief objectives while maintaining infrastructure investment efficiency.",
      "reinforcement_priority": "CRITICAL",
      "strategic_importance": 1.0
    },
    {
      "candidate_id": "cand_parallel_33_36_cap11880_c414_h980a6c",
      "explanation": "Expansion candidate cand_parallel_33_36_cap11880_c414_h980a6c was selected to improve network reinforcement capacity between 33 and 36. The expansion contributes 11880.0 MVA of additional transmission capacity with a strategic decision score of 0.00. This reinforcement supports topology robustness and congestion relief objectives while maintaining infrastructure investment efficiency.",
      "reinforcement_priority": "MODERATE",
      "strategic_importance": 0.0
    },
    {
      "candidate_id": "cand_parallel_37_64_cap11880_c331_h356a82",
      "explanation": "Expansion candidate cand_parallel_37_64_cap11880_c331_h356a82 was selected to improve network reinforcement capacity between 37 and 64. The expansion contributes 11880.0 MVA of additional transmission capacity with a strategic decision score of 1.00. This reinforcement supports topology robustness and congestion relief objectives while maintaining infrastructure investment efficiency.",
      "reinforcement_priority": "CRITICAL",
      "strategic_importance": 1.0
    },
    {
      "candidate_id": "cand_parallel_3_4_cap11880_c414_hf4ebbf",
      "explanation": "Expansion candidate cand_parallel_3_4_cap11880_c414_hf4ebbf was selected to improve network reinforcement capacity between 3 and 4. The expansion contributes 11880.0 MVA of additional transmission capacity with a strategic decision score of 0.00. This reinforcement supports topology robustness and congestion relief objectives while maintaining infrastructure investment efficiency.",
      "reinforcement_priority": "MODERATE",
      "strategic_importance": 0.0
    },
    {
      "candidate_id": "cand_parallel_48_65_cap11880_c414_v0_h534daa",
      "explanation": "Expansion candidate cand_parallel_48_65_cap11880_c414_v0_h534daa was selected to improve network reinforcement capacity between 48 and 65. The expansion contributes 11880.0 MVA of additional transmission capacity with a strategic decision score of 0.00. This reinforcement supports topology robustness and congestion relief objectives while maintaining infrastructure investment efficiency.",
      "reinforcement_priority": "MODERATE",
      "strategic_importance": 0.0
    },
    {
      "candidate_id": "cand_parallel_48_65_cap11880_c414_v1_h534daa",
      "explanation": "Expansion candidate cand_parallel_48_65_cap11880_c414_v1_h534daa was selected to improve network reinforcement capacity between 48 and 65. The expansion contributes 11880.0 MVA of additional transmission capacity with a strategic decision score of 0.00. This reinforcement supports topology robustness and congestion relief objectives while maintaining infrastructure investment efficiency.",
      "reinforcement_priority": "MODERATE",
      "strategic_importance": 0.0
    },
    {
      "candidate_id": "cand_parallel_59_60_cap11880_c414_h20e9d5",
      "explanation": "Expansion candidate cand_parallel_59_60_cap11880_c414_h20e9d5 was selected to improve network reinforcement capacity between 59 and 60. The expansion contributes 11880.0 MVA of additional transmission capacity with a strategic decision score of 0.00. This reinforcement supports topology robustness and congestion relief objectives while maintaining infrastructure investment efficiency.",
      "reinforcement_priority": "MODERATE",
      "strategic_importance": 0.0
    },
    {
      "candidate_id": "cand_parallel_62_63_cap11880_c331_h692783",
      "explanation": "Expansion candidate cand_parallel_62_63_cap11880_c331_h692783 was selected to improve network reinforcement capacity between 62 and 63. The expansion contributes 11880.0 MVA of additional transmission capacity with a strategic decision score of 1.00. This reinforcement supports topology robustness and congestion relief objectives while maintaining infrastructure investment efficiency.",
      "reinforcement_priority": "CRITICAL",
      "strategic_importance": 1.0
    },
    {
      "candidate_id": "cand_parallel_63_64_cap11880_c331_ha047ae",
      "explanation": "Expansion candidate cand_parallel_63_64_cap11880_c331_ha047ae was selected to improve network reinforcement capacity between 63 and 64. The expansion contributes 11880.0 MVA of additional transmission capacity with a strategic decision score of 1.00. This reinforcement supports topology robustness and congestion relief objectives while maintaining infrastructure investment efficiency.",
      "reinforcement_priority": "CRITICAL",
      "strategic_importance": 1.0
    },
    {
      "candidate_id": "cand_parallel_68_69_cap11880_c414_hf83bb2",
      "explanation": "Expansion candidate cand_parallel_68_69_cap11880_c414_hf83bb2 was selected to improve network reinforcement capacity between 68 and 69. The expansion contributes 11880.0 MVA of additional transmission capacity with a strategic decision score of 0.00. This reinforcement supports topology robustness and congestion relief objectives while maintaining infrastructure investment efficiency.",
      "reinforcement_priority": "MODERATE",
      "strategic_importance": 0.0
    },
    {
      "candidate_id": "cand_parallel_68_74_cap11880_c414_h8959b7",
      "explanation": "Expansion candidate cand_parallel_68_74_cap11880_c414_h8959b7 was selected to improve network reinforcement capacity between 68 and 74. The expansion contributes 11880.0 MVA of additional transmission capacity with a strategic decision score of 0.00. This reinforcement supports topology robustness and congestion relief objectives while maintaining infrastructure investment efficiency.",
      "reinforcement_priority": "MODERATE",
      "strategic_importance": 0.0
    },
    {
      "candidate_id": "cand_parallel_76_79_cap11880_c414_h27c6d6",
      "explanation": "Expansion candidate cand_parallel_76_79_cap11880_c414_h27c6d6 was selected to improve network reinforcement capacity between 76 and 79. The expansion contributes 11880.0 MVA of additional transmission capacity with a strategic decision score of 0.00. This reinforcement supports topology robustness and congestion relief objectives while maintaining infrastructure investment efficiency.",
      "reinforcement_priority": "MODERATE",
      "strategic_importance": 0.0
    },
    {
      "candidate_id": "cand_parallel_7_29_cap11880_c331_h36c98e",
      "explanation": "Expansion candidate cand_parallel_7_29_cap11880_c331_h36c98e was selected to improve network reinforcement capacity between 7 and 29. The expansion contributes 11880.0 MVA of additional transmission capacity with a strategic decision score of 1.00. This reinforcement supports topology robustness and congestion relief objectives while maintaining infrastructure investment efficiency.",
      "reinforcement_priority": "CRITICAL",
      "strategic_importance": 1.0
    },
    {
      "candidate_id": "cand_parallel_7_8_cap11880_c331_h8974c8",
      "explanation": "Expansion candidate cand_parallel_7_8_cap11880_c331_h8974c8 was selected to improve network reinforcement capacity between 7 and 8. The expansion contributes 11880.0 MVA of additional transmission capacity with a strategic decision score of 1.00. This reinforcement supports topology robustness and congestion relief objectives while maintaining infrastructure investment efficiency.",
      "reinforcement_priority": "CRITICAL",
      "strategic_importance": 1.0
    },
    {
      "candidate_id": "cand_parallel_87_88_cap11880_c414_h5ce888",
      "explanation": "Expansion candidate cand_parallel_87_88_cap11880_c414_h5ce888 was selected to improve network reinforcement capacity between 87 and 88. The expansion contributes 11880.0 MVA of additional transmission capacity with a strategic decision score of 0.00. This reinforcement supports topology robustness and congestion relief objectives while maintaining infrastructure investment efficiency.",
      "reinforcement_priority": "MODERATE",
      "strategic_importance": 0.0
    },
    {
      "candidate_id": "cand_parallel_88_89_cap11880_c414_h1a4b7e",
      "explanation": "Expansion candidate cand_parallel_88_89_cap11880_c414_h1a4b7e was selected to improve network reinforcement capacity between 88 and 89. The expansion contributes 11880.0 MVA of additional transmission capacity with a strategic decision score of 0.00. This reinforcement supports topology robustness and congestion relief objectives while maintaining infrastructure investment efficiency.",
      "reinforcement_priority": "MODERATE",
      "strategic_importance": 0.0
    },
    {
      "candidate_id": "cand_parallel_88_91_cap11880_c414_h105318",
      "explanation": "Expansion candidate cand_parallel_88_91_cap11880_c414_h105318 was selected to improve network reinforcement capacity between 88 and 91. The expansion contributes 11880.0 MVA of additional transmission capacity with a strategic decision score of 0.00. This reinforcement supports topology robustness and congestion relief objectives while maintaining infrastructure investment efficiency.",
      "reinforcement_priority": "MODERATE",
      "strategic_importance": 0.0
    },
    {
      "candidate_id": "cand_parallel_8_9_cap11880_c331_hbce51e",
      "explanation": "Expansion candidate cand_parallel_8_9_cap11880_c331_hbce51e was selected to improve network reinforcement capacity between 8 and 9. The expansion contributes 11880.0 MVA of additional transmission capacity with a strategic decision score of 1.00. This reinforcement supports topology robustness and congestion relief objectives while maintaining infrastructure investment efficiency.",
      "reinforcement_priority": "CRITICAL",
      "strategic_importance": 1.0
    },
    {
      "candidate_id": "cand_parallel_99_102_cap11880_c414_h2e3cee",
      "explanation": "Expansion candidate cand_parallel_99_102_cap11880_c414_h2e3cee was selected to improve network reinforcement capacity between 99 and 102. The expansion contributes 11880.0 MVA of additional transmission capacity with a strategic decision score of 0.00. This reinforcement supports topology robustness and congestion relief objectives while maintaining infrastructure investment efficiency.",
      "reinforcement_priority": "MODERATE",
      "strategic_importance": 0.0
    }
  ],
  "congestion_explanations": [
    {
      "hotspot_id": "primary_hotspot",
      "explanation": "Congestion hotspot primary_hotspot represents a stressed operational transmission corridor affecting 3 infrastructure edges. The hotspot exhibits an average congestion score of 0.25, indicating elevated topology stress and increased bottleneck pressure within the operational network.",
      "severity_level": "MODERATE"
    }
  ],
  "resilience_explanations": [
    {
      "vulnerability_id": "vulnerability_48",
      "explanation": "Topology vulnerability vulnerability_48 indicates structural infrastructure fragility affecting 1 critical network nodes. The vulnerability exhibits a fragmentation risk score of 0.90, suggesting elevated survivability risk under infrastructure failure or stressed operating conditions.",
      "survivability_risk": "HIGH"
    },
    {
      "vulnerability_id": "vulnerability_84",
      "explanation": "Topology vulnerability vulnerability_84 indicates structural infrastructure fragility affecting 1 critical network nodes. The vulnerability exhibits a fragmentation risk score of 0.50, suggesting elevated survivability risk under infrastructure failure or stressed operating conditions.",
      "survivability_risk": "HIGH"
    },
    {
      "vulnerability_id": "vulnerability_109",
      "explanation": "Topology vulnerability vulnerability_109 indicates structural infrastructure fragility affecting 1 critical network nodes. The vulnerability exhibits a fragmentation risk score of 0.40, suggesting elevated survivability risk under infrastructure failure or stressed operating conditions.",
      "survivability_risk": "MODERATE"
    },
    {
      "vulnerability_id": "vulnerability_99",
      "explanation": "Topology vulnerability vulnerability_99 indicates structural infrastructure fragility affecting 1 critical network nodes. The vulnerability exhibits a fragmentation risk score of 0.80, suggesting elevated survivability risk under infrastructure failure or stressed operating conditions.",
      "survivability_risk": "HIGH"
    },
    {
      "vulnerability_id": "vulnerability_76",
      "explanation": "Topology vulnerability vulnerability_76 indicates structural infrastructure fragility affecting 1 critical network nodes. The vulnerability exhibits a fragmentation risk score of 0.60, suggesting elevated survivability risk under infrastructure failure or stressed operating conditions.",
      "survivability_risk": "HIGH"
    },
    {
      "vulnerability_id": "vulnerability_70",
      "explanation": "Topology vulnerability vulnerability_70 indicates structural infrastructure fragility affecting 1 critical network nodes. The vulnerability exhibits a fragmentation risk score of 0.30, suggesting elevated survivability risk under infrastructure failure or stressed operating conditions.",
      "survivability_risk": "MODERATE"
    },
    {
      "vulnerability_id": "vulnerability_11",
      "explanation": "Topology vulnerability vulnerability_11 indicates structural infrastructure fragility affecting 1 critical network nodes. The vulnerability exhibits a fragmentation risk score of 0.70, suggesting elevated survivability risk under infrastructure failure or stressed operating conditions.",
      "survivability_risk": "HIGH"
    },
    {
      "vulnerability_id": "vulnerability_8",
      "explanation": "Topology vulnerability vulnerability_8 indicates structural infrastructure fragility affecting 1 critical network nodes. The vulnerability exhibits a fragmentation risk score of 0.20, suggesting elevated survivability risk under infrastructure failure or stressed operating conditions.",
      "survivability_risk": "MODERATE"
    },
    {
      "vulnerability_id": "vulnerability_29",
      "explanation": "Topology vulnerability vulnerability_29 indicates structural infrastructure fragility affecting 1 critical network nodes. The vulnerability exhibits a fragmentation risk score of 0.30, suggesting elevated survivability risk under infrastructure failure or stressed operating conditions.",
      "survivability_risk": "MODERATE"
    },
    {
      "vulnerability_id": "vulnerability_63",
      "explanation": "Topology vulnerability vulnerability_63 indicates structural infrastructure fragility affecting 1 critical network nodes. The vulnerability exhibits a fragmentation risk score of 0.20, suggesting elevated survivability risk under infrastructure failure or stressed operating conditions.",
      "survivability_risk": "MODERATE"
    },
    {
      "vulnerability_id": "vulnerability_64",
      "explanation": "Topology vulnerability vulnerability_64 indicates structural infrastructure fragility affecting 1 critical network nodes. The vulnerability exhibits a fragmentation risk score of 0.20, suggesting elevated survivability risk under infrastructure failure or stressed operating conditions.",
      "survivability_risk": "MODERATE"
    },
    {
      "vulnerability_id": "vulnerability_37",
      "explanation": "Topology vulnerability vulnerability_37 indicates structural infrastructure fragility affecting 1 critical network nodes. The vulnerability exhibits a fragmentation risk score of 0.20, suggesting elevated survivability risk under infrastructure failure or stressed operating conditions.",
      "survivability_risk": "MODERATE"
    },
    {
      "vulnerability_id": "vulnerability_7",
      "explanation": "Topology vulnerability vulnerability_7 indicates structural infrastructure fragility affecting 1 critical network nodes. The vulnerability exhibits a fragmentation risk score of 0.20, suggesting elevated survivability risk under infrastructure failure or stressed operating conditions.",
      "survivability_risk": "MODERATE"
    }
  ],
  "executive_summary": "The optimization workflow identified 22 strategic infrastructure expansion decisions contributing 261360.0 MVA of additional network reinforcement capacity. The resulting infrastructure plan maintains a total expansion investment cost of 85.32 while improving topology robustness, congestion relief, and operational survivability. The operational analysis identified 1 congestion hotspot regions and achieved an estimated resilience score of 0.01."
}