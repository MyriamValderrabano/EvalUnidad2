<template>
  <div class="bg-gray-200 w-full h-full min-h-screen   ">

    <form>

      <div class="mx-auto w-full lg:w-7/12  dark:bg-gray-700 p-8 lg:rounded-l-none">
        <h3 class="py-4 text-3xl font-semibold text-center text-gray-800 dark:text-white">Dispensacion</h3>
        <form class="px-8 pt-6 pb-8 mb-4 bg-white dark:bg-gray-800 rounded">
          <a href="/tablaDis"
            class="text-white bg-gradient-to-r from-red-400 via-red-500 to-red-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-red-300 dark:focus:ring-red-800 shadow-lg shadow-red-500/50 dark:shadow-lg dark:shadow-red-800/80 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2">
            Regresar
          </a>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-6">
            <div>
              <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="nombre">
                Codigo
              </label>
              <input
                class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600"
                id="nombre" type="number" placeholder="Nombre" />
            </div>
            <div>
              <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="descripcion">
                Nombre Generico
              </label>
              <input
                class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600"
                id="descripcion" type="text" placeholder="Descripción" />
            </div>
            <div>
              <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="tipo">
                Tipo de presentacion
              </label>
              <input
                class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600"
                id="tipo" type="text" placeholder="Tipo" />
            </div>
            <div>
              <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="departamento">
                Via Administrativa
              </label>
              <input
                class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600"
                id="departamento" type="text" placeholder="Departamento" />
            </div>
            <div>
              <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="cantidad_existencia">
                Cantidad
              </label>
              <input
                class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600"
                id="cantidad_existencia" type="number" placeholder="Cantidad en Existencia" />
            </div>
            <div>
              <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="cantidad_existencia">
                Costo
              </label>
              <input
                class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600"
                id="cantidad_existencia" type="number" placeholder="Cantidad en Existencia" />
            </div>
            <div>
              <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="cantidad_existencia">
                Importe
              </label>
              <input
                class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600"
                id="cantidad_existencia" type="number" placeholder="Cantidad en Existencia" />
            </div>


          </div>
          <div class="mt-6 text-center">
            <button
              class="bg-indigo-600 text-white font-semibold py-2 px-4 w-full rounded-lg hover:bg-indigo-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 "
              type="button">
              Registrar
            </button>
          </div>
        </form>
      </div>
    </form>
  </div>
</template>
  