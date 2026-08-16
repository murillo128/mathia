from __future__ import annotations

SHUFFLED_POOL = {
    "S1": "For similar triangles, corresponding lengths scale by one factor while areas scale by its square; matching the right quantity matters more than surface resemblance.",
}


def pool_id(_: int) -> str:
    return "S1"


def rev_context(n: int) -> dict[str, str]:
    return {
        "factual": f"The visible rows show a few values of multiplication modulo {n}; the table is deliberately incomplete and does not establish fibers, subset images, or orbit behavior.",
        "procedural": "For a concrete question, enumerate the requested inputs, solve the stated congruence, or iterate the finite map until a value repeats; use gcd calculations when convenient.",
        "structural": "The useful picture is information loss. A unit acts reversibly and preserves distinctions everywhere; a nonunit merges some classes. That same distinction constrains fibers and subset images, while exact orbit lengths still depend on the instance.",
        "sterile": "Finite residue systems display recurring patterns, and multiplication often creates compact cyclic pictures whose symmetry and periodicity make modular arithmetic visually and algebraically appealing.",
        "wrong": "The main driver of collisions and orbit structure is the parity of the modulus: odd moduli behave reversibly, while even moduli necessarily identify distinct residue classes.",
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
        structural = "For coprime moduli, the two residue coordinates are independent and uniquely determine the global class. Arithmetic can be carried out coordinate by coordinate and then recombined, while relations coupling the coordinates still require actual local reasoning."
        wrong = "Even for coprime moduli, the two coordinates normally leave several global possibilities, and arithmetic on the global residue cannot reliably be recovered by operating on the coordinates separately."
    else:
        structural = "With a shared factor, residue coordinates overlap: only compatible pairs occur and a compatible pair can represent several classes modulo the product. Coordinate-wise arithmetic remains valid on compatible data, but independence and uniqueness fail."
        wrong = "Shared factors are irrelevant to the coordinate representation: every local pair occurs exactly once modulo the product, just as if the moduli were coprime, and no compatibility condition is needed."
    return {
        "factual": "The visible rows encode a few integers by residues under two moduli. The table is partial and does not state reconstruction counts, polynomial images, or coupled coordinate conditions.",
        "procedural": "For any requested condition, enumerate residues modulo the product and test both coordinates. For a transformation, reconstruct x or calculate the requested residues directly and compare.",
        "structural": structural,
        "sterile": "Using several modular coordinates offers a compact alternative description of periodic arithmetic, and the resulting tables often display a striking grid-like regularity across repeated residue patterns.",
        "wrong": wrong,
    }


def composition_context() -> dict[str, str]:
    return {
        "factual": "The situation gives two affine maps on one finite residue system. Their formulas are visible, but image sizes, fixed points, and the behavior of their composition have not been computed.",
        "procedural": "Enumerate outputs for image sizes, solve h(x)=x for fixed points, and compose affine formulas by substitution before checking the resulting finite map.",
        "structural": "For affine maps, the linear coefficient controls collisions and composition multiplies those coefficients, so lost distinctions cannot be recovered later. Translation repositions outputs, but it can still change fixed points and orbit geometry even when reversibility is unchanged.",
        "sterile": "Iterating and composing affine formulas produces rich finite patterns, and small changes in coefficients or offsets can create visually different cycles that remain compact enough to tabulate.",
        "wrong": "The translation term is the main source of reversibility and dynamical structure: a suitable nonzero offset can restore bijectivity even when the multiplier itself collapses residue classes.",
    }
