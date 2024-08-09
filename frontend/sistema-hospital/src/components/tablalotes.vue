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
          <tr v-for="item in medicamentos" :key="item.id" :class="getRowClass(item)">
            <td class="px-6 py-4" :class="{'w-1/8': item.editing}">
              <span v-if="!item.editing">{{ item.nombre }}</span>
              <input v-else v-model="item.nombre" type="text" class="w-full border p-1 rounded" />
            </td>
            
            <td class="px-6 py-4" :class="{'w-1/8': item.editing}">
              <span v-if="!item.editing">{{ item.personalMedico }}</span>
              <input v-else v-model="item.personalMedico" type="text" class="w-full border p-1 rounded" />
            </td>
            
            <td class="px-6 py-4" :class="{'w-1/8': item.editing}">
              <span v-if="!item.editing">{{ item.clave }}</span>
              <input v-else v-model="item.clave" type="text" class="w-full border p-1 rounded" />
            </td>
            
            <td class="px-6 py-4" :class="{'w-1/8': item.editing}">
              <span v-if="!item.editing">{{ item.estatus }}</span>
              <input v-else v-model="item.estatus" type="text" class="w-full border p-1 rounded" />
            </td>
            
            <td class="px-6 py-4" :class="{'w-1/8': item.editing}">
              <span v-if="!item.editing">${{ item.costoTotal }}</span>
              <div v-else class="flex items-center">
                <button @click="changeValue(item, 'costoTotal', -1)" class="px-2 py-1 border rounded-l bg-gray-200 hover:bg-gray-300">-</button>
                <input v-model.number="item.costoTotal" type="number" step="0.01" min="0" class="w-20 px-2 py-1 border-t border-b text-center" />
                <button @click="changeValue(item, 'costoTotal', 1)" class="px-2 py-1 border rounded-r bg-gray-200 hover:bg-gray-300">+</button>
              </div>
            </td>
            
            <td class="px-6 py-4" :class="{'w-1/8': item.editing}">
              <span v-if="!item.editing">{{ item.cantidad }}</span>
              <div v-else class="flex items-center">
                <button @click="changeValue(item, 'cantidad', -1)" class="px-2 py-1 border rounded-l bg-gray-200 hover:bg-gray-300">-</button>
                <input v-model.number="item.cantidad" type="number" min="0" class="w-20 px-2 py-1 border-t border-b text-center" />
                <button @click="changeValue(item, 'cantidad', 1)" class="px-2 py-1 border rounded-r bg-gray-200 hover:bg-gray-300">+</button>
              </div>
            </td>
            
            <td class="px-6 py-4" :class="{'w-1/8': item.editing}">
              <span v-if="!item.editing">{{ item.ubicacion }}</span>
              <input v-else v-model="item.ubicacion" type="text" class="w-full border p-1 rounded" />
            </td>
            
            <td class="px-6 py-4">
              <span>{{ new Date(item.fechaRegistro).toLocaleString() }}</span>
            </td>
            
            <td class="px-6 py-4">
              <span v-if="!item.editing">{{ new Date(item.fechaActualizacion).toLocaleString() }}</span>
              <span v-else>{{ new Date().toLocaleString() }}</span>
            </td>
            
            <td class="px-6 py-4 text-center">
              <a href="#" v-if="!item.editing" @click.prevent="editItem(item)" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">Editar</a>
              <a href="#" v-if="!item.editing" @click.prevent="deleteItem(item.id)" class="font-medium text-red-600 dark:text-red-500 hover:underline ml-2">Eliminar</a>
              <a href="#" v-if="item.editing" @click.prevent="saveItem(item)" class="font-medium text-green-600 dark:text-green-500 hover:underline ml-2">Guardar</a>
              <a href="#" v-if="item.editing" @click.prevent="cancelEdit(item)" class="font-medium text-gray-600 dark:text-gray-500 hover:underline ml-2">Cancelar</a>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      medicamentos: [
        { id: 1, nombre: 'Paracetamol', personalMedico: 'Dr. Smith', clave: 'M123', estatus: 'Reservado', costoTotal: 100.00, cantidad: 200, ubicacion: 'Almacén 1', fechaRegistro: new Date().toISOString(), fechaActualizacion: new Date().toISOString(), editing: false },
        { id: 2, nombre: 'Ibuprofeno', personalMedico: 'Dra. García', clave: 'M456', estatus: 'En transito', costoTotal: 150.00, cantidad: 300, ubicacion: 'Almacén 2', fechaRegistro: new Date().toISOString(), fechaActualizacion: new Date().toISOString(), editing: false },
        { id: 3, nombre: 'Amoxicilina', personalMedico: 'Dr. López', clave: 'M789', estatus: 'Recibido', costoTotal: 200.00, cantidad: 500, ubicacion: 'Almacén 3', fechaRegistro: new Date().toISOString(), fechaActualizacion: new Date().toISOString(), editing: false },
        { id: 4, nombre: 'Cetirizina', personalMedico: 'Dra. Hernández', clave: 'M321', estatus: 'Rechazado', costoTotal: 80.00, cantidad: 150, ubicacion: 'Almacén 4', fechaRegistro: new Date().toISOString(), fechaActualizacion: new Date().toISOString(), editing: false }
      ]
    };
  },
  methods: {
    getRowClass(item) {
      return {
        'bg-gray-100 dark:bg-gray-800': item.editing
      };
    },
    changeValue(item, field, delta) {
      item[field] = Math.max(0, item[field] + delta);
    },
    editItem(item) {
      item.editing = true;
    },
    saveItem(item) {
      item.editing = false;
      item.fechaActualizacion = new Date().toISOString(); // Update the fechaActualizacion on save
    },
    cancelEdit(item) {
      item.editing = false;
    },
    deleteItem(id) {
      this.medicamentos = this.medicamentos.filter(item => item.id !== id);
    }
  }
};
</script>

<style scoped>
/* Add your custom styles here */
</style>
