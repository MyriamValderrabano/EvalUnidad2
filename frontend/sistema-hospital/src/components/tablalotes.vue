<template>
  <div class="min-h-screen bg-gray-200 bg-opacity-100 flex-col justify-center py-5 sm:px-6 lg:px-8 px-6 bg-repeat">
    <div class="sm:mx-auto sm:w-full sm:max-w-md">
      <img class="mx-auto h-10 w-auto" src="https://www.svgrepo.com/show/301692/login.svg" alt="Workflow">
      <h2 class="mt-6 text-center text-3xl leading-9 font-extrabold text-gray-900">
        Lotes Medicamentos
      </h2>
    </div>
    <div class="mt-6">
      <a href="/lotes"
         class="text-white bg-gradient-to-r from-cyan-400 via-cyan-500 to-cyan-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-cyan-300 dark:focus:ring-cyan-800 shadow-lg shadow-cyan-500/50 dark:shadow-lg dark:shadow-cyan-800/80 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2">
        Agregar +
      </a>
    </div>
    <div class="relative overflow-x-auto shadow-md sm:rounded-lg mt-6">
      <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
        <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
          <tr>
            <th scope="col" class="px-6 py-3">Medicamento</th>
            <th scope="col" class="px-6 py-3">Personal Médico</th>
            <th scope="col" class="px-6 py-3">Clave</th>
            <th scope="col" class="px-6 py-3">Estatus</th>
            <th scope="col" class="px-6 py-3">Costo Total</th>
            <th scope="col" class="px-6 py-3">Cantidad</th>
            <th scope="col" class="px-6 py-3">Ubicación</th>
            <th scope="col" class="px-6 py-3">Fecha de Registro</th>
            <th scope="col" class="px-6 py-3">Fecha de Actualización</th>
            <th scope="col" class="px-6 py-3 text-center">Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in medicamentos" :key="item.ID" :class="getRowClass(item)">
            <td class="px-6 py-4">
              <span v-if="!item.editing">{{ item.Medicamento_ID }}</span>
              <input v-else v-model="item.Medicamento_ID" type="text" class="w-full border p-1 rounded" />
            </td>
            <td class="px-6 py-4">
              <span v-if="!item.editing">{{ item.Personal_Medico_ID }}</span>
              <input v-else v-model="item.Personal_Medico_ID" type="text" class="w-full border p-1 rounded" />
            </td>
            <td class="px-6 py-4">
              <span v-if="!item.editing">{{ item.Clave }}</span>
              <input v-else v-model="item.Clave" type="text" class="w-full border p-1 rounded" />
            </td>
            <td class="px-6 py-4">
              <span v-if="!item.editing">{{ item.Estatus }}</span>
              <select v-else v-model="item.Estatus" class="w-full border p-1 rounded">
                <option value="Reservado">Reservado</option>
                <option value="En_transito">En transito</option>
                <option value="Recibido">Recibido</option>
                <option value="Rechazado">Rechazado</option>
              </select>
            </td>
            <td class="px-6 py-4">
              <span v-if="!item.editing">${{ item.Costo_Total }}</span>
              <div v-else class="flex items-center">
                <button @click="changeValue(item, 'Costo_Total', -1)" class="px-2 py-1 border rounded-l bg-gray-200 hover:bg-gray-300">-</button>
                <input v-model.number="item.Costo_Total" type="number" step="0.01" min="0" class="w-20 px-2 py-1 border-t border-b text-center" />
                <button @click="changeValue(item, 'Costo_Total', 1)" class="px-2 py-1 border rounded-r bg-gray-200 hover:bg-gray-300">+</button>
              </div>
            </td>
            <td class="px-6 py-4">
              <span v-if="!item.editing">{{ item.Cantidad }}</span>
              <div v-else class="flex items-center">
                <button @click="changeValue(item, 'Cantidad', -1)" class="px-2 py-1 border rounded-l bg-gray-200 hover:bg-gray-300">-</button>
                <input v-model.number="item.Cantidad" type="number" min="0" class="w-20 px-2 py-1 border-t border-b text-center" />
                <button @click="changeValue(item, 'Cantidad', 1)" class="px-2 py-1 border rounded-r bg-gray-200 hover:bg-gray-300">+</button>
              </div>
            </td>
            <td class="px-6 py-4">
              <span v-if="!item.editing">{{ item.Ubicacion }}</span>
              <input v-else v-model="item.Ubicacion" type="text" class="w-full border p-1 rounded" />
            </td>
            <td class="px-6 py-4">
              <span>{{ new Date(item.Fecha_Registro).toLocaleString() }}</span>
            </td>
            <td class="px-6 py-4">
              <span v-if="!item.editing">{{ new Date(item.Fecha_Actualizacion).toLocaleString() }}</span>
              <span v-else>{{ new Date().toLocaleString() }}</span>
            </td>
            <td class="px-6 py-4 text-center">
              <a href="#" v-if="!item.editing" @click.prevent="editItem(item)" class="font-medium text-blue-600 hover:underline">Editar</a>
              <a href="#" v-if="!item.editing" @click.prevent="deleteItem(item.ID)" class="font-medium text-red-600 hover:underline ml-2">Eliminar</a>
              <a href="#" v-if="item.editing" @click.prevent="saveItem(item)" class="font-medium text-green-600 hover:underline ml-2">Guardar</a>
              <a href="#" v-if="item.editing" @click.prevent="cancelEdit(item)" class="font-medium text-gray-600 hover:underline ml-2">Cancelar</a>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      medicamentos: []
    };
  },
  mounted() {
    this.fetchMedicamentos();
  },
  methods: {
    async fetchMedicamentos() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/lotes/');
        this.medicamentos = response.data;
      } catch (error) {
        console.error('Error fetching lotes:', error);
      }
    },
    getRowClass(item) {
      return {
        'bg-gray-100 dark:bg-gray-800': item.editing,
        'odd:bg-white odd:dark:bg-gray-900': !item.editing,
        'even:bg-gray-50 even:dark:bg-gray-800': !item.editing,
        'border-b dark:border-gray-700': !item.editing
      };
    },
    changeValue(item, field, delta) {
      if (item.editing) {
        item[field] = Math.max(0, parseFloat((item[field] + delta).toFixed(2))); // Prevenir valores negativos
      }
    },
    editItem(item) {
      item.editing = true;
    },
    async saveItem(item) {
      item.editing = false;
      item.Fecha_Actualizacion = new Date().toISOString(); // Actualiza la fecha de modificación
      try {
        await axios.put(`http://127.0.0.1:8000/lotes/${item.ID}/`, item);
        this.fetchMedicamentos(); // Refresca los datos
      } catch (error) {
        console.error('Error saving item:', error);
      }
    },
    async deleteItem(id) {
      if (confirm('¿Estás seguro de que quieres eliminar este lote?')) {
        try {
          const response = await axios.delete(`http://127.0.0.1:8000/lotes/${id}/`);
          if (response.status === 204) { // 204 No Content indica éxito en la eliminación
            this.fetchMedicamentos(); // Refresca los datos
          } else {
            console.error('Error deleting item: Unexpected response status', response.status);
          }
        } catch (error) {
          console.error('Error deleting item:', error);
        }
      }
    },
    cancelEdit(item) {
      item.editing = false;
      this.fetchMedicamentos(); // Refresca los datos para descartar cambios no guardados
    }
  }
};
</script>

<style scoped>
/* Agrega cualquier estilo adicional aquí */
</style>
