from __future__ import annotations

SHUFFLED_POOL = {
    "S1": "For similar triangles, corresponding lengths scale by one factor while areas scale by its square; matching the right quantity matters more than surface resemblance.",
}


def pool_id(_: int) -> str:
    return "S1"


def rev_context(n: int) -> dict[str, str]:
    return {
        "factual": f"The visible rows show a few values of multiplication modulo {n}; the table is deliberately incomplete and does not establish the behavior on every residue class.",
        "procedural": "For a new multiplier, compute its gcd with the modulus or enumerate the finite map; for a congruence, count residues satisfying the equation directly.",
        "structural": "The key question is information loss: multiplication is reversible exactly when its multiplier is a unit. Invertible multipliers preserve distinctions; nonunits collapse residue classes.",
        "sterile": "Finite residue systems often display regular repeating patterns, and multiplication can produce visually organized cycles whose symmetry makes modular arithmetic compact and aesthetically appealing.",
        "wrong": "Reversibility is controlled mainly by parity of the modulus: odd moduli support reversible multiplication, whereas even moduli necessarily force collisions among residue classes.",
    }


def gcd_context() -> dict[str, str]:
    return {
        "factual": "The visible material replaces one integer pair by another of the form (b, a-qb). No gcd value is supplied, and the coefficient q may be signed.",
        "procedural": "To answer a numerical gcd question, run Euclid's algorithm or enumerate common divisors. For a proposed transformation, compute both gcd values and compare them.",
        "structural": "The move (a,b)->(b,a-qb) preserves exactly the common-divisor information: each old common divisor divides the new pair, and the reverse relation reconstructs a.",
        "sterile": "Integer pairs admit many equivalent-looking descriptions, and repeated arithmetic transformations often reveal orderly patterns that make elementary number theory feel unexpectedly unified and economical.",
        "wrong": "Gcd preservation requires q to be the ordinary Euclidean quotient and the resulting remainder to be nonnegative and smaller than b; signed or oversized remainders break it.",
    }


def crt_context(coprime: bool) -> dict[str, str]:
    if coprime:
        structural = "For coprime moduli, the two residue coordinates are independent: together they retain all information modulo the product, so each coordinate pair determines one product-residue class."
        wrong = "Even for coprime moduli, two residue coordinates generally describe several product-residue classes; uniqueness requires one modulus to divide the other or an extra constraint."
    else:
        structural = "When the moduli share a factor, the two residue coordinates are constrained by their overlap. Some pairs are impossible and some product-residue classes share the same coordinates."
        wrong = "Shared factors do not affect residue coordinates: every pair of local residues still occurs exactly once modulo the product, just as in the coprime case."
    return {
        "factual": "The visible rows encode a few integers by their residues under two moduli. The table is partial and does not state how many distinct coordinate pairs exist.",
        "procedural": "To test a residue pair, scan x modulo the product and check both congruences. To study the encoding, enumerate all product residues and compare coordinate pairs.",
        "structural": structural,
        "sterile": "Using several modular coordinates offers a compact alternative description of periodic arithmetic, and the resulting tables often display a striking grid-like regularity across repeated residue patterns.",
        "wrong": wrong,
    }


def composition_context() -> dict[str, str]:
    return {
        "factual": "The situation gives two affine maps on one finite residue system. Their formulas are visible, but the composition and image sizes have not been computed for you.",
        "procedural": "Reduce coefficients modulo n, enumerate outputs to get image sizes, and compose affine formulas by substitution. A full output table can verify any proposed permutation claim.",
        "structural": "For affine maps, translation only repositions outputs; information loss is controlled by the linear coefficient. Composition multiplies those coefficients, so lost distinctions cannot be repaired later.",
        "sterile": "Iterating and composing affine formulas produces rich finite patterns, and small changes in coefficients can create visually different cycles that nevertheless remain easy to tabulate.",
        "wrong": "The translation term is the main source of reversibility in an affine map: a suitable nonzero offset can restore bijectivity even when the multiplier collapses residues.",
    }
