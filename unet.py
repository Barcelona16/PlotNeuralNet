
import sys
sys.path.append('../')
from pycore.tikzeng import *
from pycore.blocks  import *

arch = [ 
    to_head('..'), 
    to_cor(),
    to_begin(),
    
    #input
    to_input( 'brain.jpg' ),
    to_input( 'gd.jpg' ,to = "(68,0,0)" ),

    #block-001
    to_ConvConvRelu( name='ccr_b1', s_filer=500, n_filer=(64,64), offset="(0,0,0)", to="(0,0,0)", width=(2,2), height=40, depth=40  ),
    to_Pool(name="pool_b1", offset="(0,0,0)", to="(ccr_b1-east)", width=1, height=32, depth=32, opacity=0.5),
    
    *block_2ConvPool( name='b2', botton='pool_b1', top='pool_b2', s_filer=128, n_filer=128, offset="(5,-10,0)", size=(32,32,3.5), opacity=0.5 ),
    *block_2ConvPool( name='b3', botton='pool_b2', top='pool_b3', s_filer=128, n_filer=256, offset="(5,-10,0)", size=(25,25,4.5), opacity=0.5 ),
    *block_2ConvPool( name='b4', botton='pool_b3', top='pool_b4', s_filer=64,  n_filer=512, offset="(5,-10,0)", size=(16,16,5.5), opacity=0.5 ),
    *block_Unconv( name="bb1", botton="pool_b2", top='', s_filer=64,  n_filer=512, offset="(5.1,10,0)", size=(40,40,2.5), opacity=0.5 ),
    *block_Unconv( name="bb2", botton="pool_b3", top='', s_filer=64,  n_filer=512, offset="(5.1,10,0)", size=(32,32,3.5), opacity=0.5 ),
    *block_Unconv( name="bb3", botton="pool_b4", top='', s_filer=64,  n_filer=512, offset="(5.1,10,0)", size=(25,25,4.5), opacity=0.5 ),

    *block_Unconv( name="bb4", botton="ccr_res_bb2", top='', s_filer=64,  n_filer=512, offset="(5.1,10,0)", size=(40,40,2.5), opacity=0.5 ),
    *block_Unconv( name="bb5", botton="ccr_res_bb3", top='', s_filer=64,  n_filer=512, offset="(5.1,10,0)", size=(32,32,3.5), opacity=0.5 ),
    *block_Unconv( name="bb6", botton="ccr_res_bb5", top='', s_filer=64,  n_filer=512, offset="(5.1,10,0)", size=(40,40,4.5), opacity=0.5 ),
    #Bottleneck
    #block-005
     to_ConvConvRelu( name='ccr_b5', s_filer=32, n_filer=(1024,1024), offset="(5,-10,0)", to="(pool_b4-east)", width=(8,8), height=8, depth=8, caption="Bottleneck"  ),
     to_connection( "pool_b4", "ccr_b5"),
    # to_skip( of='ccr_b1', to='ccr_res_bb1', pos=1.25),
    # to_skip( of='ccr_b1', to='ccr_res_bb4', pos=1.45),
    # to_skip( of='ccr_b1', to='ccr_res_bb6', pos=1.65),

    # to_skip( of='ccr_res_c_bb1', to='ccr_res_bb4', pos=1.25),
    # to_skip( of='ccr_res_c_bb4', to='ccr_res_bb6', pos=1.25),
    # to_skip( of='ccr_res_c_bb6', to='ccr_res_b9', pos=1.25),
    # to_skip( of='ccr_b2', to='ccr_res_c_bb2', pos=1.25),
    # to_skip( of='ccr_res_c_bb2', to='ccr_res_c_bb5', pos=1.25),
    # to_skip( of='ccr_res_c_bb5', to='ccr_res_b8', pos=1.25),
    # to_skip( of='ccr_b3', to='ccr_res_c_bb3', pos=1.25),
    # to_skip( of='ccr_res_c_bb3', to='ccr_res_b7', pos=1.25),
    #Decoder
    *block_Unconv( name="b6", botton="ccr_b5", top='end_b6', s_filer=64,  n_filer=512, offset="(5.1,10,0)", size=(16,16,5.0), opacity=0.5 ),
    #to_skip( of='ccr_b4', to='ccr_res_b6', pos=1.25),
    *block_Unconv( name="b7", botton="end_b6", top='end_b7', s_filer=128, n_filer=256, offset="(5.1,10,0)", size=(25,25,4.5), opacity=0.5 ),
    #to_skip( of='ccr_b3', to='ccr_res_b7', pos=1.25),    
    *block_Unconv( name="b8", botton="end_b7", top='end_b8', s_filer=256, n_filer=128, offset="(5.1,10,0)", size=(32,32,3.5), opacity=0.5 ),
    #to_skip( of='ccr_b2', to='ccr_res_b8', pos=1.25),    
    
    *block_Unconv( name="b9", botton="end_b8", top='end_b9', s_filer=512, n_filer=64,  offset="(5.1,10,0)", size=(40,40,2.5), opacity=0.5 ),
    #to_skip( of='ccr_b1', to='ccr_res_b9', pos=1.25),
    
    to_ConvSoftMax( name="soft1", s_filer=512, offset="(0.75,0,0)", to="(end_b9-east)", width=1, height=40, depth=40, caption="SOFT" ),
    to_connection( "end_b9", "soft1"),
     
    to_end() 
    ]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
    
