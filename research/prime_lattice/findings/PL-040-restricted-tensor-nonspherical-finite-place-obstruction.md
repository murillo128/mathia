# PL-040 — Restricted-tensor automorphic scattering confines non-spherical prime data to finitely many places

## Claim

The most immediate non-spherical repair left open by `PL-039` does not produce a new operator-valued carrier across the infinitely many prime directions of the exponent lattice.

For a standard adelic principal-series/Eisenstein construction over `Q`, the finite-place representation and its smooth vectors are built as a **restricted tensor product** with respect to distinguished unramified spherical vectors. Consequently, every fixed smooth restricted-tensor vector is spherical at all but finitely many finite primes. If `S` contains the archimedean place together with every finite place where the inducing data or chosen vector is non-spherical/ramified, then the global standard intertwiner factors schematically as

```text
M(s) f_s
  = [product_{p notin S} c_p(s)]
    x [spherical tensor outside S]
    x [finite tensor/product of local intertwiners at S].
```

At `p notin S`, `c_p(s)` is exactly the scalar unramified Gindikin--Karpelevich factor. In the ordinary trivial `GL_2`/modular channel these factors multiply, in the Euler-product half-plane, to the same partial zeta ratio that underlies the spherical scattering coefficient of `PL-039`; after the archimedean completion and Eisenstein continuation one recovers the classical completed scalar scattering datum. Normalized global formulas make the separation explicit: the global L-function ratio is scalar, while genuinely non-spherical normalized local operators occur only at the finite exceptional set `S`.

Therefore the route

```text
ordinary zeta spherical scattering
+ choose finite-level K-types / ramified or nonspherical finite-place vectors
    -> operator-valued datum coupling infinitely many prime directions
    -> new rigidity for the Riemann divisor
```

fails at its first structural step. For any fixed smooth finite-level automorphic section, the non-spherical finite-place operator content is supported on only finitely many primes. The infinitely many ordinary prime Euler factors remain in the same scalar L-factor normalization.

This is **not** a theorem that finite local matrix factors can never participate in a stronger global positivity argument. It is the narrower exact obstruction needed for the current prime-lattice search: merely leaving the spherical vector inside the standard restricted-tensor Eisenstein representation does not turn the Riemann Euler product into a joint infinite-prime matrix invariant.

**Evidence/status:** `LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the stated route of using a fixed smooth finite-level standard automorphic/Eisenstein channel as the non-spherical operator-valued escape from `PL-039`.

Restricted tensor products and almost-everywhere unramified local components are classical automorphic-representation theory (Flath). The separation of global L-function normalizing factors from finitely many exceptional normalized local intertwiners is classical Langlands--Shahidi/intertwining theory and is explicit in Hundley's formulas. The derived contribution is only the research-line consequence: standard finite-level non-spherical data cannot supply the missing **infinite-prime operator coupling** because it differs from the spherical channel at finitely many prime coordinates.

## Restricted tensor products force finite exceptional support

Let

```text
I(s) = tensor'_v I_v(s)
```

be an adelic induced representation, with the restricted tensor product taken with respect to normalized spherical vectors `f^o_{p,s}` at almost every finite prime. By definition, a pure tensor in the restricted product has

```text
f_{p,s} = f^o_{p,s}
```

for all but finitely many `p`. A general vector is a finite linear combination of such pure tensors, hence there is still a finite set `S_f` outside which every tensor occurring in that vector uses the distinguished spherical component.

The same almost-everywhere unramified structure holds representation-theoretically. Flath's tensor-product theorem writes an irreducible admissible automorphic representation as a restricted tensor product of local representations, with a nonzero hyperspecial-fixed vector at almost every finite place. For classical finite-level forms this is concrete: adelization is invariant under `GL_2(Z_p)` at every prime not dividing the level.

In prime-exponent language this matters because the coordinates indexed by rational primes are literally the directions whose energies are `log p`. A fixed smooth automorphic vector may enrich finitely many such directions, but outside a finite exceptional set its local state is forced back onto the one-dimensional spherical line audited in `PL-039`.

## Global intertwining separates the infinite scalar from finite local operator data

For a factorable section, the standard global intertwining integral factors into local standard intertwiners. Away from `S`, the local action on the normalized spherical vector is

```text
M_p(s) f^o_{p,s}
  = c_p(s) f^o_{p,w s},
```

where `w` is the relevant Weyl element and `c_p` is the unramified ratio of local L-factors.

Hundley's global formula makes the useful normalization pattern explicit. For a finite set `S` containing the ramified and archimedean places, the global intertwiner on a factorizable vector is a scalar product of global/partial L-function ratios multiplied by normalized local intertwiners at the places in `S`; outside `S` only the normalized spherical vectors remain. Schematically,

```text
global standard intertwiner
  = scalar global L-ratio
    x product_{v in S} normalized local operator_v
    x spherical transport outside S.
```

In the trivial rank-one channel over `Q`, the finite unramified scalar is, initially in its absolute-convergence region,

```text
product_{p notin S} c_p(u)
  = zeta^S(u) / zeta^S(u+1),
```

with `zeta^S` denoting the Euler factors outside `S`. The finitely many omitted local factors and the real place produce the usual finite correction/completion. In the modular parameter `u=2s-1`, this is the same scalar mechanism that becomes

```text
Lambda(2s-1) / Lambda(2s)
```

in the classical Eisenstein scattering coefficient.

Thus the global object can certainly be operator-valued on the exceptional local spaces, but its structure has the form

```text
infinite-prime zeta-sensitive part
    = scalar L-factor product;

non-spherical matrix/operator part
    = finitely supported local correction for a fixed vector/level.
```

That is exactly the distinction that the proposed non-spherical repair would have needed to avoid.

## Analytic-continuation boundary

The displayed product over `p notin S` is an Euler product only in the usual absolute-convergence half-plane. Nothing here licenses termwise continuation into the critical strip.

As in `PL-039`, meromorphic continuation of the global scattering/intertwining datum comes from Eisenstein-series and standard-intertwiner theory. The restricted-tensor decomposition is an algebraic/representation-theoretic statement about local components; the continued global L-factor is supplied by automorphic analytic continuation.

Accordingly, the conclusion survives continuation in the correct sense: after continuation, the same normalized global intertwining theory separates scalar L-data from finitely many exceptional local operators. It is not obtained by pretending the infinite Euler product converges in the strip.

## Relation to the exponent lattice

For the positive-integer lattice,

```text
log n = sum_p v_p(n) log p.
```

The hoped-for escape after `PL-039` was that non-spherical local representation spaces might turn each prime coordinate into a genuinely matrix-valued degree of freedom, leaving a global operator invariant that coupled the full family `{log p}` and constrained the scalar zeta channel.

The restricted tensor product blocks that naive move. A fixed smooth vector has the form

```text
[nonspherical data at finitely many p]
  tensor
[spherical distinguished vector at every remaining p].
```

Hence it does not attach independent non-spherical matrix data to the full infinite exponent lattice. At almost every prime, the local state again lies on the one-dimensional spherical line, and its zeta dependence is the scalar `c_p` already isolated in `PL-039`.

This is stronger than a Beurling-control objection. The failure occurs inside the canonical rational-prime automorphic representation itself: standard smooth adelic representation theory permits only finitely many exceptional finite-place components in any one restricted-tensor vector.

## Archimedean K-types do not repair the missing prime coupling

Over `Q` there is one archimedean place. Nonzero weight or other archimedean K-type data can change the real local intertwiner and hence gamma/rational factors in the completed scattering coefficient. Roy--Schmidt--Yi explicitly treat classical Eisenstein series of varying weight and level adelically and compute their local/global intertwiners.

This is genuine additional structure, but it is not an infinite family of prime-coordinate matrix degrees of freedom: it is data at the single real place. It may be essential for completion and symmetry, as `PL-014` already emphasizes, but merely adding an archimedean K-type to standard Eisenstein scattering does not undo the finite-support statement at the finite primes.

## Adversarial checks and boundaries

### Non-spherical local operators can genuinely be matrix-valued

At an exceptional finite place, Iwahori-fixed or other non-spherical spaces may have dimension greater than one and standard intertwiners can act by nontrivial matrices. This finding does not deny that local operator structure.

The obstruction is about support: for a fixed smooth global vector/level, such components occur at only finitely many finite primes. They therefore do not by themselves create a joint matrix-valued object over the entire prime-exponent lattice.

### Finite local factors are not claimed to have a finite zero set

A rational function of `p^{-s}` may have infinitely many periodically repeated zeros or poles as a function of `s`. Therefore no argument here relies on counting zeros of the finite exceptional factors, and no claim is made that they could never cancel or create infinitely many points in a divisor.

The exact information-loss statement is different: finite exceptional local factors do not encode independent operator data at infinitely many rational primes. Any proposed localization theorem using them must introduce and prove an additional global coupling; it does not arise from restricted-tensor factorization itself.

### Varying the level over an infinite family is outside this no-go

One can consider an ensemble of automorphic representations with unbounded conductors so that, across the family, every prime is eventually exceptional. Trace formulas and families of levels may then generate genuinely global information.

That construction is not a single standard Riemann-zeta scattering channel with a fixed non-spherical vector. It adds a new ensemble/trace structure and would have to prove why the resulting global relation constrains the ordinary level-one zeta scalar rather than merely studying a larger family. Such a mechanism is not ruled out here.

### Infinite nonspherical tensors require a new analytic object

The Hilbert completion of an infinite tensor product may contain vectors not represented by a single algebraic restricted tensor with finite exceptional support. But the ordinary smooth automorphic representation, Eulerian Eisenstein section, and standard factorized intertwining formulas used to obtain the zeta L-factor are built from the restricted tensor product.

A proposal using infinitely many genuinely nonspherical local components must therefore re-establish existence, topology/domain, scattering/intertwining factorization, meromorphic continuation, and canonicity. It cannot be advertised as the standard finite-level automorphic completion already present in `PL-039`.

### Target-relative constructions remain open

The Nyman/model-space branch of the accepted clue is not a restricted-tensor Eisenstein vector. A target-relative operator may couple all prime directions through a global Hardy-space condition, a model-space projection, or a positivity/trace identity. `PL-040` does not address such a mechanism.

## Prior art and novelty audit

The structural ingredients are established prior art:

- **D. Flath**, “Decomposition of representations into tensor products,” in *Automorphic Forms, Representations and L-functions*, Proc. Sympos. Pure Math. **33**, Part 1 (1979), 179–183, DOI `10.1090/pspum/033.1/546596`. This is the classical restricted-tensor-product theorem for irreducible admissible adelic representations, with almost all local components unramified.
- **Joseph Hundley**, “Holomorphy of adjoint L functions for quasisplit A2,” *Research in Number Theory* **4** (2018), Article 44, DOI `10.1007/s40993-018-0136-8`. Beyond the local spherical formula already used in `PL-039`, his global intertwining formula chooses a finite set `S` containing the ramified places and separates the global L-ratio from normalized local operators at `S`.
- **Manami Roy, Ralf Schmidt, Shaoyun Yi**, “Classical and adelic Eisenstein series,” arXiv:`2109.07649` [math.NT] (2021). Their explicit classical/adelic dictionary records that finite-level forms are spherical away from the level and develops local/global intertwining calculations for weight, level, and character variants.
- **Keys--Shahidi** and **Heiermann**, already recorded for `PL-039`, provide the general normalization/global-spherical context.

No novelty is claimed for restricted tensor products, almost-everywhere unramifiedness, local/global factorization, or normalized intertwiners. The only durable contribution is the negative synthesis for the current line: **ordinary finite-level non-spherical standard scattering changes finitely many prime coordinates and therefore does not evade the infinite-prime scalarization identified in `PL-039`.**

A search of adjacent automorphic/intertwining literature found the restricted-product and finite-`S` separation as standard structure, not a hidden operator invariant tying non-spherical local matrices across all rational primes. This classicalizes the naive non-spherical escape rather than supporting a novelty claim.

## Falsification / escape tests

The obstruction would be materially escaped by a construction that proves all of the following, rather than merely choosing extra local vectors:

1. the ordinary Riemann-zeta problem canonically forces non-spherical operator data at **infinitely many** finite primes, or a genuinely global operator that cannot be reduced to finitely many exceptional local factors times the scalar zeta normalization;
2. that infinite/global datum is mathematically defined with the required topology/domains and survives the analytic continuation used in the critical strip;
3. after standard L-factor normalization it remains nontrivial and is not freely engineerable by choosing local vectors or level;
4. it imposes a positivity, normality, trace, determinant, or other falsifiable constraint on the ordinary spherical zeta divisor stronger than the already-known functional equation/scattering unitarity.

A target-relative Nyman/model-space construction or a genuinely global trace/positivity mechanism could in principle pass these tests. A fixed finite-level K-type/ramified Eisenstein section does not.

## Consequence for the research line

The operator-valued escape chain is now narrower:

```text
unramified spherical standard intertwiner
    -> one-dimensional at every prime
    -> zeta data is scalar L-normalization                 [PL-039]

fixed finite-level nonspherical/ramified standard section
    -> non-spherical at finitely many finite primes only
    -> finite local operator correction x same scalar
       infinite-prime L-normalization                      [PL-040]
```

Thus the next useful search should not be “add K-types/ramification to the standard Eisenstein vector.” It must look for a **genuinely global or target-relative coupling** whose information content is not finitely supported in the prime coordinates and whose mathematics actually constrains the scalar zeta channel.