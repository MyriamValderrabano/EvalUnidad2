<template>
    <div class="bg-gray-200 w-full h-full min-h-screen   ">

        <form>

            <div class="mx-auto w-full lg:w-7/12  dark:bg-gray-700 p-8 lg:rounded-l-none">
                <h3 class="py-4 text-3xl font-semibold text-center text-gray-800 dark:text-white">Medicamentos</h3>
                <form class="px-8 pt-6 pb-8 mb-4 bg-white dark:bg-gray-800 rounded">
                    <a href="/tablamedic"
                        class="text-white bg-gradient-to-r from-red-400 via-red-500 to-red-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-red-300 dark:focus:ring-red-800 shadow-lg shadow-red-500/50 dark:shadow-lg dark:shadow-red-800/80 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2">
                        Regresar
                    </a>

                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-6">
                        <div>
                            <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="codigo">
                                Codigo
                            </label>
                            <input
                                class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600"
                                id="codigo" type="number" placeholder="XXXXXXXXX" />
                        </div>
                        <div>
                            <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="nombre">
                                Nombre Generico
                            </label>
                            <input
                                class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600"
                                id="nombreGen" type="text" placeholder="" />
                        </div>
                        <div>
                            <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="tipo">
                                Nombre Comercial
                            </label>
                            <input
                                class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600"
                                id="nombreCom" type="text" placeholder="" />
                        </div>
                        <div>
                            <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white"
                                for="departamento">
                                Tipo de Presentacion
                            </label>
                            <div class="mt-1 relative rounded-md shadow-sm">
                                <select id="genero" name="genero" required
                                    class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600">
                                    <option value="" disabled selected>Selecciona tipo</option>
                                    <option value="comprimidos">Comprimidos</option>
                                    <option value="grageas">Grageas</option>
                                    <option value="capsulas">Cápsulas</option>
                                    <option value="jarabes">Jarabes</option>
                                    <option value="gotas">Gotas</option>
                                    <option value="solucion">Solución</option>
                                    <option value="pomada">Pomada</option>
                                    <option value="jabon">Jabon</option>
                                    <option value="supositorios">Supositorios</option>
                                    <option value="viales">Viales</option>
                                    <option value="suspension">Suspensión</option>
                                    <option value="polvo">Polvo</option>

                                    <!-- Agrega más opciones según tus necesidades -->
                                </select>
                            </div>

                        </div>
                        <div>
                            <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white"
                                for="cantidad_existencia">
                                Via de Administracion
                            </label>
                            <div class="mt-1 relative rounded-md shadow-sm">
                                <select id="via" name="via" required
                                    class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600">
                                    <option value="" disabled selected>Selecciona via</option>
                                    <option value="oral">Oral</option>
                                    <option value="intravenoso">Intravenoso</option>
                                    <option value="rectal">Rectal</option>
                                    <option value="cutaneo">Cutáneo</option>
                                    <option value="subcutaneo">Subcutáneo</option>
                                    <option value="oftalmica">Oftálmica</option>
                                    <option value="otica">Ótica</option>
                                    <option value="nasal">Nasal</option>
                                    <option value="topica">Tópica</option>
                                    <option value="parental">Parental</option>


                                    <!-- Agrega más opciones según tus necesidades -->
                                </select>
                            </div>
                        </div>
                        <div>
                            <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="codigo">
                                Cantidad
                            </label>
                            <input
                                class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600"
                                id="cantidad" type="number" placeholder="" />
                        </div>
                        <div>
                            <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="codigo">
                                Precio Costo
                            </label>
                            <input
                                class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600"
                                id="costo" type="number" placeholder="" />
                        </div>
                        <div>
                            <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="codigo">
                                Precio Venta
                            </label>
                            <input
                                class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600"
                                id="venta" type="number" placeholder="" />
                        </div>
                        <div>
                            <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white"
                                for="cantidad_existencia">
                                Estatus
                            </label>
                            <div class="mt-1 relative rounded-md shadow-sm">
                                <select id="estatus" name="estatus" required
                                    class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600">
                                    <option value="" disabled selected>Selecciona estatus</option>
                                    <option value="disponible">Disponible</option>
                                    <option value="no_disponible">No disponible</option>



                                    <!-- Agrega más opciones según tus necesidades -->
                                </select>
                            </div>
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
    