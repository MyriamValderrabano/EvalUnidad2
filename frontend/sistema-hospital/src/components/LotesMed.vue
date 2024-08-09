<template>
  <div class="bg-gray-200 w-full h-full min-h-screen">
    <div class="mx-auto w-full lg:w-7/12 dark:bg-gray-700 p-8 lg:rounded-l-none">
      <h3 class="py-4 text-3xl font-semibold text-center text-gray-800 dark:text-white">Lotes Medicamentos</h3>
      <form @submit.prevent="submitForm" class="px-8 pt-6 pb-8 mb-4 bg-white dark:bg-gray-800 rounded">
        <a href="/tablalot"
          class="text-white bg-gradient-to-r from-red-400 via-red-500 to-red-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-red-300 dark:focus:ring-red-800 shadow-lg shadow-red-500/50 dark:shadow-lg dark:shadow-red-800/80 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2">
          Regresar
        </a>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-6">
          <div>
            <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="medicamento">
              Medicamento
            </label>
            <select v-model="form.Medicamento_ID" id="medicamento" class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600">
              <option value="">--Selecciona el Medicamento--</option>
              <option value="1">Medicamento 1</option>
              <option value="2">Medicamento 2</option>
              <option value="3">Medicamento 3</option>
            </select>
          </div>

          <div>
            <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="medico">
              Personal Medico
            </label>
            <select v-model="form.Personal_Medico_ID" id="medico" class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600">
              <option value="">--Selecciona el Personal Medico--</option>
              <option value="1">Cedula 1</option>
              <option value="2">Cedula 2</option>
              <option value="3">Cedula 3</option>
            </select>
          </div>

          <div>
            <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="clave">
              Clave
            </label>
            <input v-model="form.Clave" type="text" id="clave" class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600">
          </div>

          <div>
            <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="estatus">
              Estatus
            </label>
            <select v-model="form.Estatus" id="estatus" class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600">
              <option value="">--Selecciona el Estatus--</option>
              <option value="Reservado">Reservado</option>
              <option value="En_transito">En transito</option>
              <option value="Recibido">Recibido</option>
              <option value="Rechazado">Rechazado</option>
            </select>
          </div>

          <div>
            <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="costo">
              Costo Total
            </label>
            <input v-model.number="form.Costo_Total" type="number" id="costo" step="0.01" min="0" class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600">
          </div>

          <div>
            <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="cantidad">
              Cantidad
            </label>
            <input v-model.number="form.Cantidad" type="number" id="cantidad" min="0" class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600">
          </div>

          <div>
            <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="ubicacion">
              Ubicación
            </label>
            <input v-model="form.Ubicacion" type="text" id="ubicacion" class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600">
          </div>
        </div>

        <div class="mt-6 text-center">
          <button type="submit" class="bg-indigo-600 text-white font-semibold py-2 px-4 w-full rounded-lg hover:bg-indigo-500 focus:outline-none focus:ring-2 focus:ring-indigo-500">
            Crear
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      form: {
        Medicamento_ID: '',
        Personal_Medico_ID: '',
        Clave: '',
        Estatus: '', // Debe coincidir con los valores del Enum en el backend
        Costo_Total: null,
        Cantidad: null,
        Ubicacion: '',
        Fecha_Registro: new Date().toISOString(),
        Fecha_Actualizacion: new Date().toISOString()
      }
    }
  },
  methods: {
    async submitForm() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/lotes/', this.form);
        console.log('Lote creado:', response.data);
        // Aquí puedes agregar lógica adicional como redirigir al usuario o mostrar un mensaje
      } catch (error) {
        console.error('Error al crear el lote:', error.response ? error.response.data : error.message);
        // Maneja el error, por ejemplo, mostrando un mensaje al usuario
      }
    }
  }
}
</script>

<style scoped>
/* Puedes agregar estilos aquí si es necesario */
</style>
