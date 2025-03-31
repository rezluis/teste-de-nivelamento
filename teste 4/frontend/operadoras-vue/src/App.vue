<template>
  <div class="container">
    <h1>Buscar Operadoras</h1>
    <input
      v-model="busca"
      @input="buscar"
      placeholder="Digite o nome da operadora"
    />
    <ul>
      <li v-for="operadora in resultados" :key="operadora.Registro_ANS">
        {{ operadora.Nome_Fantasia }} (CNPJ: {{ operadora.CNPJ }})
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      busca: "",
      resultados: [],
    };
  },
  methods: {
    async buscar() {
      if (this.busca.length < 3) {
        this.resultados = [];
        return;
      }
      const response = await axios.get(
        `http://127.0.0.1:8000/buscar?query=${this.busca}`
      );
      this.resultados = response.data.resultados;
    },
  },
};
</script>

<style>
.container {
  max-width: 600px;
  margin: auto;
  text-align: center;
}
input {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
}
</style>
