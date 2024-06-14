<template>
<div class=" bg-lime-200 flex flex-col justify-center py-5 sm:px-6 lg:px-8 px-6">
        <div class="sm:mx-auto sm:w-full sm:max-w-md">
            <img class="mx-auto h-10 w-auto" src="https://www.svgrepo.com/show/301692/login.svg" alt="Workflow">
            <h2 class="mt-6 text-center text-3xl leading-9 font-extrabold text-gray-900">
                Usuario
            </h2>
        </div>


        <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
            <div class="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
                <form>
                    
            

                    <div>
                        <label for="text" class="block text-sm font-medium leading-5  text-gray-700">Nombre de Usuario</label>
                        <div class="mt-1 relative rounded-md shadow-sm">
                            <input id="user" name="name" type="text" required value=""
                                class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md placeholder-gray-400 focus:outline-none focus:shadow-outline-blue focus:border-blue-300 transition duration-150 ease-in-out sm:text-sm sm:leading-5">

                        </div>
                    </div>

                    <div>
                        <label for="password" class="block text-sm font-medium leading-5 text-gray-700">Contraseña</label>
                        <div class="mt-1 rounded-md shadow-sm">
                            <input id="password" name="password" type="password" required
                                class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md placeholder-gray-400 focus:outline-none focus:shadow-outline-blue focus:border-blue-300 transition duration-150 ease-in-out sm:text-sm sm:leading-5">
                        </div>
                    </div>

                    <div>
                        <label for="password" class="block text-sm font-medium leading-5 text-gray-700">Repetir Contraseña</label>
                        <div class="mt-1 rounded-md shadow-sm">
                            <input id="repetir_password" name="password" type="password" required
                                class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md placeholder-gray-400 focus:outline-none focus:shadow-outline-blue focus:border-blue-300 transition duration-150 ease-in-out sm:text-sm sm:leading-5">
                        </div>
                    </div>
                   
                    <div class="mt-6">
                        <span class="block w-full rounded-md shadow-sm">

                            <a href="/"
                            class="w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-blue-500 hover:bg-blue-700 focus:outline-none focus:border-indigo-700 focus:shadow-outline-indigo active:bg-indigo-700 transition duration-150 ease-in-out">
                                Iniciar
                            </a>
                         
                        </span>
                    </div>
                    <div class="mt-6">
                        <span class="block w-full rounded-md shadow-sm">

                            <a href="/"
                            class="w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-red-500 hover:bg-red-700 focus:outline-none focus:border-indigo-700 focus:shadow-outline-indigo active:bg-indigo-700 transition duration-150 ease-in-out">Cancelar
                            </a>
                         
                        </span>
                    </div>
                    
                </form>

            </div>
        </div>
    </div>
</template>