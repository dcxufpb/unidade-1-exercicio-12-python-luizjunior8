
import pytest
import departamento


def verifica_campo_obrigatorio_objeto(mensagem_esperada, departamento):
    with pytest.raises(Exception) as excinfo:
        departamento.dados_departamento()
    the_exception = excinfo.value
    assert mensagem_esperada == str(the_exception)

NOME_DEPARTAMENTO = "Depto. test."
SIGLA = "D1"
LOCALIZACAO = "Local 1"
NOME_COORDENADOR = "Coord. 1"
IDADE = 40
CPF = "111.222.333-44"

COORDENADOR_COMPLETO = departamento.Coordenador(NOME_COORDENADOR, IDADE, CPF)
DEPARTAMENTO_COMPLETO = departamento.Departamento(NOME_DEPARTAMENTO, SIGLA, LOCALIZACAO, COORDENADOR_COMPLETO)

TEXTO_ESPERADO_DEPARTAMENTO_COMPLETO = """Depto. test., D1
End.: Local 1
Coord. 1
40 anos
CPF: 111.222.333-44"""

def test_departamento_completo():
    assert (DEPARTAMENTO_COMPLETO.dados_departamento() == TEXTO_ESPERADO_DEPARTAMENTO_COMPLETO)


NOME_VAZIO = departamento.Departamento("", SIGLA , LOCALIZACAO, COORDENADOR_COMPLETO)
NOME_NULO = departamento.Departamento(None, SIGLA , LOCALIZACAO, COORDENADOR_COMPLETO)

MENSAGEM_NOME_OBRIGATORIO = "O campo nome do departamento é obrigatório"

def test_validacao_nome():
    verifica_campo_obrigatorio_objeto(MENSAGEM_NOME_OBRIGATORIO, NOME_NULO)
    verifica_campo_obrigatorio_objeto(MENSAGEM_NOME_OBRIGATORIO, NOME_VAZIO)


SIGLA_NULA = departamento.Departamento(NOME_DEPARTAMENTO, None, LOCALIZACAO, COORDENADOR_COMPLETO)
SIGLA_VAZIA = departamento.Departamento(NOME_DEPARTAMENTO, "", LOCALIZACAO, COORDENADOR_COMPLETO)

TEXTO_ESPERADO_SEM_SIGLA = """Depto. test.
End.: Local 1
Coord. 1
40 anos
CPF: 111.222.333-44"""

def test_departamento_sem_sigla():
    assert (SIGLA_VAZIA.dados_departamento() == TEXTO_ESPERADO_SEM_SIGLA)

def test_departamento_sigla_nula():
    assert (SIGLA_NULA.dados_departamento() == TEXTO_ESPERADO_SEM_SIGLA)


LOCAL_VAZIO = departamento.Departamento(NOME_DEPARTAMENTO, SIGLA , "", COORDENADOR_COMPLETO)
LOCAL_NULO = departamento.Departamento(NOME_DEPARTAMENTO, SIGLA , None, COORDENADOR_COMPLETO)

MENSAGEM_LOCALIZACAO_OBRIGATORIA = "O campo localização do departamento é obrigatório"

def test_validacao_local():
    verifica_campo_obrigatorio_objeto(MENSAGEM_LOCALIZACAO_OBRIGATORIA, LOCAL_NULO)
    verifica_campo_obrigatorio_objeto(MENSAGEM_LOCALIZACAO_OBRIGATORIA, LOCAL_VAZIO)

NOME_COORD_VAZIO = departamento.Coordenador("", IDADE, CPF)
NOME_COORD_NULO = departamento.Coordenador(None, IDADE, CPF)
DEPTO_NOME_COORD_VAZIO = departamento.Departamento(NOME_DEPARTAMENTO, SIGLA, LOCALIZACAO, NOME_COORD_VAZIO)
DEPTO_NOME_COORD_NULO = departamento.Departamento(NOME_DEPARTAMENTO, SIGLA, LOCALIZACAO, NOME_COORD_NULO)

MENSAGEM_NOME_COORD_OBRIGATORIO = "O nome do coordenador é obrigatório"

def test_valida_nome_coord():
    verifica_campo_obrigatorio_objeto(MENSAGEM_NOME_COORD_OBRIGATORIO, DEPTO_NOME_COORD_VAZIO)
    verifica_campo_obrigatorio_objeto(MENSAGEM_NOME_COORD_OBRIGATORIO, DEPTO_NOME_COORD_NULO)


IDADE_NULA = departamento.Coordenador(NOME_COORDENADOR, None, CPF)
IDADE_VAZIA = departamento.Coordenador(NOME_COORDENADOR, "", CPF)
COORD_IDADE_NULA = departamento.Departamento(NOME_DEPARTAMENTO, SIGLA, LOCALIZACAO, IDADE_NULA)
COORD_IDADE_VAZIA = departamento.Departamento(NOME_DEPARTAMENTO, SIGLA, LOCALIZACAO, IDADE_VAZIA)

TEXTO_ESPERADO_SEM_IDADE = """Depto. test., D1
End.: Local 1
Coord. 1
CPF: 111.222.333-44"""

def test_coordenador_sem_idade():
    assert (COORD_IDADE_VAZIA.dados_departamento() == TEXTO_ESPERADO_SEM_IDADE)

def test_coordenador_idade_nula():
    assert (COORD_IDADE_NULA.dados_departamento() == TEXTO_ESPERADO_SEM_IDADE)


CPF_COORD_VAZIO = departamento.Coordenador(NOME_COORDENADOR, IDADE, "")
CPF_COORD_NULO = departamento.Coordenador(NOME_COORDENADOR, IDADE, None)
DEPTO_CPF_COORD_VAZIO = departamento.Departamento(NOME_DEPARTAMENTO, SIGLA, LOCALIZACAO, CPF_COORD_VAZIO)
DEPTO_CPF_COORD_NULO = departamento.Departamento(NOME_DEPARTAMENTO, SIGLA, LOCALIZACAO, CPF_COORD_NULO)

MENSAGEM_CPF_COORD_OBRIGATORIO = "O cpf do coordenador é obrigatório"

def test_valida_cpf_coord():
    verifica_campo_obrigatorio_objeto(MENSAGEM_CPF_COORD_OBRIGATORIO, DEPTO_CPF_COORD_VAZIO)
    verifica_campo_obrigatorio_objeto(MENSAGEM_CPF_COORD_OBRIGATORIO, DEPTO_CPF_COORD_NULO)


IDADE_E_SIGLA_VAZIAS = departamento.Departamento(NOME_DEPARTAMENTO, None, LOCALIZACAO, IDADE_VAZIA)

TEXTO_ESPERADO_SEM_IDADE_SEM_SIGLA = """Depto. test.
End.: Local 1
Coord. 1
CPF: 111.222.333-44"""

def test_idade_e_sigla_vazias():
    assert (IDADE_E_SIGLA_VAZIAS.dados_departamento() == TEXTO_ESPERADO_SEM_IDADE_SEM_SIGLA)