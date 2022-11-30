import React from "react";

function CreateFilme() {
    return (
        <body>
    <div class="container-sm" style={{marginTop: "25px"}}>
        <h2>Cadastrar novo filme</h2>
        
    
        <form >
            <div class="mb-3">
                <label for="exampleInputEmail1">Nome</label>
                <input type="text" class="form-control" id="filme_nome" name="filme_nome" placeholder="Nome do filme"/>
            </div>
           
            <div class="container" style={{padding: "0"}}>
                <div class="row">
                    <div class="col">
                        
                        <div class="mb-3">
                            <label for="exampleInputPassword1">Categoria</label>
                            <select class="form-select" aria-label="Categoria" id="filme_categoria"
                                name="filme_categoria">
                                <option disabled selected value>Selecione uma das categorias</option>
                                <option value="Ação">Ação</option>
                                <option value="Aventura">Aventura</option>
                                <option value="Cinema de arte">Cinema de arte</option>
                                <option value="Chanchada">Chanchada</option>
                                <option value="Comédia">Comédia</option>
                                <option value="Comédia de ação">Comédia de ação</option>
                                <option value="Comédia de terror">Comédia de terror</option>
                                <option value="Comédia dramática">Comédia dramática</option>
                                <option value="Comédia romântica">Comédia romântica</option>
                                <option value="Dança">Dança</option>
                                <option value="Documentário">Documentário</option>
                                <option value="Docuficção">Docuficção</option>
                                <option value="Drama">Drama</option>
                                <option value="Espionagem">Espionagem</option>
                                <option value="Faroeste">Faroeste</option>
                                <option value="Fantasia">Fantasia</option>
                                <option value="Fantasia científica">Fantasia científica</option>
                                <option value="Ficção científica">Ficção científica</option>
                                <option value="Filmes com truques">Filmes com truques</option>
                                <option value="Filmes de guerra">Filmes de guerra</option>
                                <option value="Mistério">Mistério</option>
                                <option value="Musical">Musical</option>
                                <option value="Filme policial">Filme policial</option>
                                <option value="Romance">Romance</option>
                                <option value="Terror">Terror</option>
                                <option value="Thriller">Thriller</option>
                            </select>
                        </div>
                    </div>
                    <div class="col">
                        <div class="mb-3">
                            <label for="exampleInputPassword1">Censura</label>
                            <select class="form-select" aria-label="Categoria" id="filme_censura"
                                name="filme_censura">
                                <option disabled selected value>Selecione uma das opções</option>
                                <option value="LIVRE (L)">LIVRE (L)</option>
                                <option value="Não recomendado para menores de 10 (dez) anos">Não recomendado para menores de 10 (dez) anos</option>
                                <option value="Não recomendado para menores de 12 (doze) anos">Não recomendado para menores de 12 (doze) anos</option>
                                <option value="Não recomendado para menores de 14 (quatorze) anos">Não recomendado para menores de 14 (quatorze) anos</option>
                                <option value="Não recomendado para menores de 16 (quatorze) anos">Não recomendado para menores de 16 (quatorze) anos</option>
                                <option value="Não recomendado para menores de 18 (quatorze) anos">Não recomendado para menores de 18 (quatorze) anos</option>
                            </select>
                        </div>
                    </div>
                </div>
            </div>

            <div class="mb-3">
                <label for="exampleInputPassword1">Empresa Produtora</label>
                <input type="text" class="form-control" id="filme_empresa_produtora" name="filme_empresa_produtora"
                    placeholder="Empresa produtora"/>
            </div>
            <div class="form-check mb-3">
                <input class="form-check-input" type="checkbox" value="" id="filme_nacional" name="filme_nacional"/>
                <label class="form-check-label" for="flexCheckDefault">
                    Filme Nacional
                </label>
            </div>
            <div class="mb-3">
                <label for="exampleInputPassword1">Duração</label>
                <input type="text" class="form-control" id="filme_duracao" name="filme_duracao" placeholder="Duração"/>
            </div>
            <button type="submit" class="btn btn-primary">Adicionar filme</button>
        </form>
    </div>
    
</body>
    )
}

export default CreateFilme;