#define MIN_ALLOC_SIZE 4096

typedef struct header {
    unsigned int size;
    struct block *next;
} header_t;

static void add_to_free_list(header_t *bp) {
    header_t *p;
    for(p = freep;!(bp > p && bp < p->next);p = p->next)
        if (p >= p->next && (bp > p || bp < p->next))
            break;
    if(bp + bp->size == p->next) {
        bp->size += p->
    }
}

static header_t* morecore(size_t num_units) {
    void *vp;
    header_t *up;
    if(num_units < MIN_ALLOC_SIZE)
        num_units = MIN_ALLOC_SIZE / sizeof(header_t);
    if (vp = sbrk(num_units * sizeof(header_t))) == (void*) -1)
        return NULL;
}

int main(int argc,char **argv) {

}
