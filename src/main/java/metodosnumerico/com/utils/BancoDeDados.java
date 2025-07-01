package metodosnumerico.com.utils;

public class BancoDeDados {
    private boolean criptografado;
    private boolean possuiBackup;
    private String chaveCriptografia;

    public BancoDeDados(boolean possuiBackup) {
        this.possuiBackup = possuiBackup;
        this.criptografado = false;
    }

    public void criptografar(String chave) {
        this.criptografado = true;
        this.chaveCriptografia = chave;
    }

    public void descriptografar() {
        this.criptografado = false;
        this.chaveCriptografia = null;
    }

    public boolean isCriptografado() {
        return criptografado;
    }

    public boolean possuiBackup() {
        return possuiBackup;
    }
}

