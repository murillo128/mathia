# PL-251 — Finite-dimensional Artin representation functors always split the principal zeta isotypic factor

## Claim

The live frontier after `PL-249` and `PL-250` asks whether a source-forced **nonlinear** cross-character operation can keep the richer Frobenius data of a finite Galois/class-field cover coupled to the principal Riemann-zeta channel. A large canonical class of such nonlinear operations can now be ruled out exactly: any construction that still lands in the finite-dimensional complex representation category of the finite Galois group preserves a canonical trivial-isotypic direct summand, and ordinary Artin `L`-functions turn that summand into a multiplicatively separate power of the base zeta function.

Let `E/Q` be a finite Galois extension with finite group `G`, and let `W` be any finite-dimensional complex representation of `G`. Define the averaging projector

`P_G = |G|^(-1) sum_(g in G) W(g)`.

Then `P_G` commutes with `G`, `im(P_G)=W^G`, and

`W = W^G direct-sum ker(P_G)`.

If `m=dim W^G`, then `W^G` is exactly `m` copies of the trivial representation, so with `W_0=ker(P_G)` one has the canonical decomposition

`W = 1^m direct-sum W_0`, `W_0^G=0`.

Artin formalism therefore gives, first in the half-plane of absolute Euler-product convergence,

`L_Q(s,W) = zeta(s)^m L_Q(s,W_0)`.

The factorization is local and includes ramified primes: inertia invariants commute with the direct sum, and the local determinant factors blockwise. By Brauer induction the corresponding Artin functions admit meromorphic continuation, so the equality survives as a meromorphic identity. For virtual representations the same statement holds in the representation ring with integer trivial multiplicity.

Consequently tensor products, duals, tensor powers, symmetric powers, exterior powers, Schur functors and finite combinations of these operations do **not** by themselves produce an irreducibly mixed principal-zeta channel. They can create new nontrivial Artin factors and can change the multiplicity of the trivial constituent, but whenever the Riemann zeta factor occurs it remains the Artin factor of a canonical direct summand.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT + NO-NOVELTY-CLAIM` for the route

`finite Galois Frobenius data -> canonical finite-dimensional representation functor -> ordinary Artin L readout -> nonlinear cross-character mixing of the principal zeta block -> RH localization`.

The representation theory and Artin formalism are classical. The durable line-specific content is the closure of the explicit nonlinear escape left open by `PL-250`: merely replacing the regular representation by a canonical tensor/dual/Schur construction does not evade principal-block splitting.

## 1. The invariant projector is canonical and already performs the split

No basis, Frobenius representative, or character-table choice is needed. Since the ground field has characteristic zero,

`P_G^2=P_G` and `W(h)P_G=P_GW(h)=P_G` for every `h in G`.

Hence `im(P_G)=W^G`, while `ker(P_G)` is a `G`-stable complement. This is the canonical trivial-isotypic projection associated with the group action itself. In particular, if a nonlinear operation `F` on input representations produces another finite-dimensional representation

`W=F(V_1,...,V_r)`,

then the question “does this operation couple something into the principal character?” reduces exactly to whether `W^G` is nonzero. If it is, those invariant vectors split off as copies of `1`; if it is not, the ordinary Artin `L`-function of `W` contains no trivial constituent at all.

This is stronger than the abelian character-line decomposition used in `PL-250`. The argument does not require `G` to be abelian and does not require decomposing all of `W` into irreducibles. It only projects onto the piece relevant to the principal zeta channel.

## 2. Artin factorization is exact place by place

For a finite place `p`, the Artin local factor is

`L_p(s,W)=det(1-W(Frob_p)p^(-s) | W^(I_p))^(-1)`,

with the usual interpretation on inertia invariants. Because

`W^(I_p) = (W^G)^(I_p) direct-sum W_0^(I_p) = W^G direct-sum W_0^(I_p)`,

the determinant is block diagonal. Frobenius acts as the identity on `W^G`, so

`L_p(s,W)=(1-p^(-s))^(-m) L_p(s,W_0)`.

Multiplication over the primes gives `zeta(s)^m L(s,W_0)` for `Re(s)>1`. Thus the splitting is not an artefact of character notation or of ignoring ramification: it is already present in every local determinant.

For a virtual character `X` in `R(G)`, additivity of characters becomes multiplicativity of Artin `L`-functions. Writing the coefficient of the trivial irreducible as `m=<X,1>`, one obtains the same identity with `m in Z`; negative multiplicities merely move zeta to the denominator. Brauer induction supplies meromorphic continuation of Artin `L`-functions, so uniqueness of meromorphic continuation extends the factorization beyond the Euler-product half-plane. Nothing here continues the Euler product termwise into the critical strip.

## 3. The strongest elementary nonlinear test already collapses: dual pairing

Take an irreducible complex representation `rho:G->GL(V)`. The canonical nonlinear pairing with its contragredient gives

`rho tensor rho^vee ~= End(V)`,

where `G` acts by conjugation. Schur's lemma identifies the invariant subspace with the scalar endomorphisms:

`End(V)^G = C I`.

The averaging projector is explicitly the projection onto that line, and one has

`rho tensor rho^vee = 1 direct-sum Ad^0(rho)`.

Therefore

`L(s,rho tensor rho^vee) = zeta(s) L(s,Ad^0(rho))`.

This is an especially useful matched control for the current research mandate. It is a genuinely source-forced cross-representation operation; its local traces contain products of Frobenius matrix coefficients and are not obtained by simply retaining the original character blocks independently. Nevertheless, the principal component is still an exact direct Artin factor.

For an abelian one-dimensional character `chi`, the collapse is maximal:

`chi tensor chi^(-1)=1`,

so at every unramified prime

`chi(Frob_p) chi(Frob_p)^(-1)=1`

and

`L(s,chi tensor chi^(-1))=zeta(s)`.

Thus the most canonical nonlinear pairing between two conjugate character channels can erase the nontrivial Frobenius phase completely rather than transport it into zeta.

## 4. The nonabelian regular representation gives the same obstruction at full-cover level

For an arbitrary finite group,

`C[G] ~= direct-sum_(rho in Irr(G)) rho^(direct-sum dim rho)`.

Hence the standard Artin factorization of the Dedekind zeta function of `E` is

`zeta_E(s)=L(s,C[G])=prod_(rho in Irr(G)) L(s,rho)^(dim rho)`.

The trivial representation occurs once and contributes `zeta_Q(s)`; all nontrivial Frobenius representation data live in the companion Artin factors. This removes the abelian restriction in the direct-sum obstruction of `PL-250` at the level relevant here.

More importantly, applying any finite sequence of standard representation-category functors to these blocks does not change the structural conclusion. Tensoring can create new invariant tensors, exterior or symmetric powers can create invariant lines, and Schur functors can change multiplicities, but `P_G` always projects those invariants to a genuine trivial direct summand before the Artin determinant is formed.

The obstruction is therefore not “characters happen to diagonalize an abelian cover.” It is finite-dimensional semisimplicity plus the multiplicative Artin formalism.

## 5. What this does and does not say about zeros

The identity

`L(s,W)=zeta(s)^m L(s,W_0)`

is a factorization of meromorphic functions, not a theorem that the zero divisor of the product is the disjoint union of the two zero divisors. In the general nonabelian case Artin holomorphy is not known, and poles of `L(s,W_0)` could in principle cancel zeros of the explicit zeta factor. No uncancelled-zero claim is being made without an additional holomorphy theorem.

This caveat actually sharpens the line boundary. The finite representation construction supplies the factorization but not the independent analytic rigidity needed by the RH target. A theorem proving holomorphy, positivity, a sign condition, or a divisor inequality for the **whole coupled arithmetic object** could still force a consequence for zeta. Such a theorem would be genuinely extra global structure; it would not arise merely from applying a representation functor.

Likewise, functional equations do not repair the route by themselves. Completed Artin factors carry their own duality and central line, but the direct-sum formalism continues to split the trivial representation. Symmetry about `Re(s)=1/2` is not the missing sign/localization theorem.

## 6. Prior-art and novelty audit

The ingredients are established classical representation theory and Artin formalism.

- **Richard Foote, V. Kumar Murty**, “Zeros and poles of Artin L-series,” *Mathematical Proceedings of the Cambridge Philosophical Society* **105**(1) (1989), 5–11. DOI `10.1017/S0305004100001316`. The paper works explicitly with Artin `L(s,chi)` for virtual characters, records the absolutely convergent definition in `Re(s)>1`, and invokes Brauer's theorem for meromorphic continuation. This is the main virtual-character/analytic-continuation audit anchor.
- **Andrew V. Sutherland**, “Sato-Tate distributions,” *Contemporary Mathematics* **740** (2019), DOI `10.1090/conm/740/14904`. Remark 1.4 states explicitly that decomposition of a finite-image complex Galois representation into subrepresentations gives the corresponding factorization of its Artin `L`-function, and illustrates that a fixed trivial line contributes the Riemann zeta factor.
- The averaging projector, semisimple decomposition of finite-group representations over `C`, Schur's lemma, and the regular-representation decomposition are standard finite-group representation theory. They are used here as exact derivations, not presented as new results.

The external search also found standard representation-ring formulations in the Stark-conjecture and equivariant-`L` literature, where Artin leading terms define multiplicative/exponential homomorphisms on `R(G)`. That confirms that packaging Artin formalism at representation-ring level is prior art rather than a novel construction.

Internal duplication was checked against `PL-115`, `PL-116`, `PL-117`, `PL-249`, and `PL-250`. `PL-115` and `PL-116` treat conjugacy/central scalarization, `PL-117` treats compatible l-adic systems and local purity, and `PL-250` proves the abelian regular-cover block split while explicitly leaving nonlinear relations open. The present delta is narrower and new to the stored line: **all finite-dimensional representation-valued nonlinear functors remain inside a category where the principal trivial isotypic component splits canonically and Artin formalism preserves that split**.

No mathematical novelty is claimed beyond this line-specific route classification.

## 7. Adversarial boundaries

1. **Not every nonlinear arithmetic invariant is representation-valued.** Determinants coupling several representations, regulators, periods, heights, cohomological pairings, nonlinear trace-formula distributions, or arithmetic intersection data need not factor through a single finite-dimensional object of `Rep_C(G)` and are outside this no-go.
2. **Canonical non-equivariant operators remain outside.** An arithmetic construction could select a preferred correspondence or target that fails to commute with `G` and therefore mixes isotypic components. The burden is to derive that symmetry breaking from the source rather than insert a programmable matrix.
3. **Infinite-dimensional and nonsemisimple settings are not covered.** Standard finite-dimensional complex Artin representations are semisimple. Infinite-dimensional representations, derived categories, extensions in other coefficient categories, or genuinely nonsemisimple monodromy can carry data absent from this argument. Finite-dimensional virtual alternating sums, however, remain inside `R(G)` and retain the zeta-power split.
4. **A global theorem can still couple factor divisors externally.** The algebraic direct sum does not prove statistical or analytic independence of the Artin factors. A source-derived positivity/duality theorem for a larger object could relate them and have a principal-zeta consequence.
5. **No Artin-holomorphy assumption is smuggled in.** Meromorphic continuation is enough for the identity; it is not enough to forbid cancellation between factors.
6. **The argument does not create an RH mechanism.** It is a decisive negative only for using ordinary finite-dimensional representation functors plus their standard Artin `L`-readout as the missing cross-character coupling.

## Research implication

The frontier after `PL-250` can be narrowed further. “Use tensor products / duals / symmetric powers / exterior powers of the retained Artin blocks” is no longer a live escape by itself. Even the canonical dual-pair coupling `rho tensor rho^vee`, which is about as natural a nonlinear cross-character construction as one can form, splits as `1 direct-sum Ad^0(rho)` and therefore leaves zeta as an ordinary principal factor.

A viable next construction must do at least one of the following: produce a source-forced nonlinear invariant that **does not factor through a finite-dimensional Artin representation**, derive a canonical symmetry-breaking operator whose off-diagonal principal/nonprincipal blocks cannot be gauged away, or prove a global positivity/duality/divisor theorem whose conclusion genuinely transfers information from the richer Artin factors into the principal zeta divisor. In every case an independent sign/localization mechanism is still required to single out `Re(s)=1/2` rather than merely recover the usual functional-equation symmetry.