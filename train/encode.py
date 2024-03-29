# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 18:20:46 2020

@author: kanishk
"""

import torch


class AtomEncoder(torch.nn.Module):

    def __init__(self, emb_dim,a_embed):
        super(AtomEncoder, self).__init__()
        
        self.atom_embedding_list = torch.nn.ModuleList()
        
        full_atom_feature_dims=[a_embed,a_embed,a_embed,a_embed,a_embed,a_embed]
        
        for i, dim in enumerate(full_atom_feature_dims):
            emb = torch.nn.Embedding(dim, emb_dim)
            torch.nn.init.xavier_uniform_(emb.weight.data)
            self.atom_embedding_list.append(emb)

    def forward(self, x):
        #print('sup')
        x_embedding = 0

        if x.dim() == 1:
           x = x.unsqueeze(1)

        x=x.type(torch.LongTensor)
        x=x.cuda()
        for i in range(x.shape[1]):
            x_embedding += self.atom_embedding_list[i](x[:,i])

        return x_embedding


class BondEncoder(torch.nn.Module):
    
    def __init__(self, emb_dim,a_embed):
        super(BondEncoder, self).__init__()
        
        self.bond_embedding_list = torch.nn.ModuleList()
        full_bond_feature_dims=[a_embed,a_embed]
        
        for i, dim in enumerate(full_bond_feature_dims):
            emb = torch.nn.Embedding(dim, emb_dim)
            torch.nn.init.xavier_uniform_(emb.weight.data)
            self.bond_embedding_list.append(emb)

    def forward(self, edge_attr):
        
        if edge_attr.dim() == 1:
            edge_attr = edge_attr.unsqueeze(1)


        bond_embedding = 0
        for i in range(edge_attr.shape[1]):
            bond_embedding += self.bond_embedding_list[i](edge_attr[:,i])

        return bond_embedding   

