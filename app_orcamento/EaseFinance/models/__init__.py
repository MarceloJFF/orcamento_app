from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


TIPO_SOLICITACAO = (
(1, 'Realocao do Orcamento Interno das Despesas no Setor'),
(2, 'Compras ou Despesas em Geral'),
(3, 'Transferencia de Valores de  Orcamento entre Setores')
)

from .Empresa import Empresa
from .Despesa import Despesa
from.OrcamentoAnual import OrcamentoAnual
from.Setor import Setor
from.OrcamentoDespesaSetor import OrcamentoDespesaSetor
from.OrcamentoSetorAno import OrcamentoSetorAno
from.Perfil import Perfil
from.Solicitacao import Solicitacao
from.Funcionario import Funcionario
from.Gestor import Gestor