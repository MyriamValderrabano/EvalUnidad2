<template>
   <div class="min-h-screen bg-lime-200 flex flex-col justify-center py-5 sm:px-6 lg:px-8 px-6">
        <div class="sm:mx-auto sm:w-full sm:max-w-md">
            <img class="mx-auto h-10 w-auto" src="https://www.svgrepo.com/show/301692/login.svg" alt="Workflow">
            <h2 class="mt-6 text-center text-3xl leading-9 font-extrabold text-gray-900">
                Personas
            </h2>
        </div>


        <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
            <div class="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
                <form>
                    <div>
                        <label for="text" class="block text-sm font-medium leading-5  text-gray-700">Nombre</label>
                        <div class="mt-1 relative rounded-md shadow-sm">
                            <input id="name" name="name" type="text" required value=""
                                class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md placeholder-gray-400 focus:outline-none focus:shadow-outline-blue focus:border-blue-300 transition duration-150 ease-in-out sm:text-sm sm:leading-5">

                        </div>
                    </div>
                    <div>
                        <label for="text" class="block text-sm font-medium leading-5  text-gray-700">Primer apellido</label>
                        <div class="mt-1 relative rounded-md shadow-sm">
                            <input id="primer_apellido" name="name" type="text" required value=""
                                class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md placeholder-gray-400 focus:outline-none focus:shadow-outline-blue focus:border-blue-300 transition duration-150 ease-in-out sm:text-sm sm:leading-5">

                        </div>
                    </div>
                    <div>
                        <label for="text" class="block text-sm font-medium leading-5  text-gray-700">Segundo
                            apellido</label>
                        <div class="mt-1 relative rounded-md shadow-sm">
                            <input id="segundo_apellido" name="name" type="text" required value=""
                                class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md placeholder-gray-400 focus:outline-none focus:shadow-outline-blue focus:border-blue-300 transition duration-150 ease-in-out sm:text-sm sm:leading-5">

                        </div>
                    </div>
                    <div>
                        <label for="text" class="block text-sm font-medium leading-5  text-gray-700">CURP</label>
                        <div class="mt-1 relative rounded-md shadow-sm">
                            <input id="curp" name="name" type="text" required value=""
                                class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md placeholder-gray-400 focus:outline-none focus:shadow-outline-blue focus:border-blue-300 transition duration-150 ease-in-out sm:text-sm sm:leading-5">

                        </div>
                    </div>
                    <div>
                        <label for="genero" class="block text-sm font-medium leading-5 text-gray-700">Género</label>
                        <div class="mt-1 relative rounded-md shadow-sm">
                            <select id="genero" name="genero" required
                                class="block w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:shadow-outline-blue focus:border-blue-300 transition duration-150 ease-in-out sm:text-sm sm:leading-5">
                                <option value="" disabled selected>Selecciona un género</option>
                                <option value="hombre">Hombre</option>
                                <option value="mujer">Mujer</option>
                                <option value="otro">Otro</option>
                                <!-- Agrega más opciones según tus necesidades -->
                            </select>
                        </div>
                    </div>

                    <div>
                        <label for="genero" class="block text-sm font-medium leading-5 text-gray-700">Tipo de sangre</label>
                        <div class="mt-1 relative rounded-md shadow-sm">
                            <select id="genero" name="genero" required
                                class="block w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:shadow-outline-blue focus:border-blue-300 transition duration-150 ease-in-out sm:text-sm sm:leading-5">
                                <option value="" disabled selected>Selecciona un grupo</option>
                                <option value="A+">A+</option>
                                <option value="A-">A-</option>
                                <option value="B+">B+</option>
                                <option value="B-">B-</option>
                                <option value="AB+">AB+</option>
                                <option value="AB-">AB-</option>
                                <option value="O+">O+</option>
                                <option value="O-">O-</option>
                                <!-- Agrega más opciones según tus necesidades -->
                            </select>
                        </div>
                    </div>
                    <div>
                        <label for="text" class="block text-sm font-medium leading-5  text-gray-700">Fecha de
                            nacimiento</label>
                        <div class="mt-1 relative rounded-md shadow-sm">
                            <input id="fecha_nacimiento" name="name" type="date" required value=""
                                class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md placeholder-gray-400 focus:outline-none focus:shadow-outline-blue focus:border-blue-300 transition duration-150 ease-in-out sm:text-sm sm:leading-5">

                        </div>
                    </div>
                    <div>
                        <label for="text" class="block text-sm font-medium leading-5  text-gray-700">Telefono</label>
                        <div class="mt-1 relative rounded-md shadow-sm">
                            <input id="name" name="name" type="tel" required value=""
                                class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md placeholder-gray-400 focus:outline-none focus:shadow-outline-blue focus:border-blue-300 transition duration-150 ease-in-out sm:text-sm sm:leading-5">

                        </div>
                    </div>

                    <div>
                        <label for="email" class="block text-sm font-medium leading-5  text-gray-700">Correo
                            electronico</label>
                        <div class="mt-1 relative rounded-md shadow-sm">
                            <input id="email" name="email" placeholder="user@example.com" type="email" required value=""
                                class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md placeholder-gray-400 focus:outline-none focus:shadow-outline-blue focus:border-blue-300 transition duration-150 ease-in-out sm:text-sm sm:leading-5">

                        </div>
                    </div>
                    <div class="mt-6">
                        <span class="block w-full rounded-md shadow-sm">

                            <a href="/"
                            class="w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-blue-500 hover:bg-blue-700 focus:outline-none focus:border-indigo-700 focus:shadow-outline-indigo active:bg-indigo-700 transition duration-150 ease-in-out">
                                Crear
                            </a>
                         
                        </span>
                    </div>
                </form>

            </div>
        </div>
    </div>
</template>