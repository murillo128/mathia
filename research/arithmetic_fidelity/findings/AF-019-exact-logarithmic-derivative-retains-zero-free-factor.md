# AF-019 — Exact logarithmic derivative is faithful modulo scale; principal parts are only divisor data

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`

## Claim

Let `Omega` be a connected complex domain and let `f,g` be nonzero meromorphic functions on `Omega`. Write

\[
L_f=\frac{f'}{f}.
\]

Then the logarithmic derivative defines a strictly finer fidelity layer than the zero/pole divisor.

1. **The exact logarithmic derivative determines a meromorphic function up to one nonzero constant.** If
   \[
   L_f=L_g
   \]
   as meromorphic functions on `Omega`, then
   \[
   \boxed{g=Cf,\qquad C\in\mathbb C^*.}
   \]
   One retained nonzero normalization value fixes `C` and therefore determines the exact function. No finite-order hypothesis is needed.

2. **The polar principal parts of the logarithmic derivative are exactly divisor data.** At a zero of `f` of order `m`, `L_f` has a simple pole with residue `+m`; at a pole of `f` of order `m`, it has a simple pole with residue `-m`. Hence retaining only the pole locations and principal parts of `L_f` is equivalent to retaining the zero/pole divisor with multiplicity.

3. **For same-divisor functions, the information discarded by principal-part compression is the logarithmic derivative of the zero-free factor.** If `f` and `g` have the same divisor, then
   \[
   h=\frac{g}{f}
   \]
   extends to a holomorphic nowhere-zero function on `Omega`, and
   \[
   \boxed{L_g-L_f=\frac{h'}{h}.}
   \]
   Thus the exact logarithmic derivative still detects variation in the zero-free multiplicative factor that the divisor does not.

4. **For normalized Euler products, the exact logarithmic derivative is faithful to the unordered generator-norm multiset.** Under the hypotheses of AF-017, let
   \[
   Z_Q(s)=\prod_j(1-q_j^{-s})^{-1}.
   \]
   If two such Euler products have equal exact logarithmic derivatives on a common absolute-convergence half-plane, then
   \[
   Z_Q=Z_R
   \]
   there and hence `Q=R` as multisets. The only generic scale ambiguity is removed intrinsically by the Euler-product normalization
   \[
   Z_Q(\sigma)\to1\qquad(\sigma\to+\infty).
   \]

5. **Grosswald--Schnitzer controls separate exact logarithmic-derivative data from divisor data.** For their modified Euler products
   \[
   \zeta^*(s)=\phi(s)\zeta(s),
   \]
   with `phi` holomorphic and nonvanishing in `Re(s)>0`,
   \[
   \boxed{
   \frac{\zeta^{*\prime}}{\zeta^*}
   -\frac{\zeta'}{\zeta}
   =\frac{\phi'}{\phi}.
   }
   \]
   The two functions have the same divisor in that half-plane, so their logarithmic derivatives have identical pole/residue data, while the exact logarithmic derivatives retain the holomorphic defect `phi'/phi`.

The resulting category hierarchy is

\[
\text{exact Euler-product function}
\longrightarrow
\text{exact logarithmic derivative}
\longrightarrow
\text{polar principal parts}
\equiv
\text{divisor}.
\]

For normalized Euler products the first two layers are both faithful to the generator-norm multiset under AF-017's hypotheses; the final divisor layer is not.

## Derivation

### Equality of exact logarithmic derivatives leaves only scale

Assume

\[
\frac{f'}{f}=\frac{g'}{g}.
\]

A zero or pole of a meromorphic function of order `m` contributes residue `+m` or `-m`, respectively, to its logarithmic derivative. Equality therefore forces `f` and `g` to have the same divisor in `Omega`.

Consequently

\[
h=\frac{g}{f}
\]

has removable singularities at every common zero or pole and extends to a holomorphic nowhere-zero function on all of `Omega`. Away from the divisor,

\[
\frac{h'}{h}
=
\frac{g'}{g}-\frac{f'}{f}
=0.
\]

By holomorphic continuation this holds everywhere. Since `Omega` is connected, `h` is constant, so

\[
\boxed{g=Cf.}
\]

Conversely, multiplication by any nonzero constant leaves `f'/f` unchanged. Hence the fiber of the exact logarithmic-derivative map is exactly the multiplicative scale orbit.

If `s_0` lies outside the common divisor and one also retains

\[
f(s_0)=g(s_0)\ne0,
\]

then `C=1`. Thus a single nonzero value is a complete lift of this residual gauge.

This is a stronger recovery statement than AF-018's divisor-only theorem in one respect: no finite-order or reflection assumption is needed because the exact logarithmic derivative has retained more of the zero-free factor before compression.

### Principal parts forget the holomorphic part

Near a zero `a` of order `m`, write

\[
f(s)=(s-a)^m u(s),\qquad u(a)\ne0.
\]

Then

\[
\frac{f'}{f}(s)
=\frac{m}{s-a}+\frac{u'}{u}(s),
\]

where `u'/u` is holomorphic near `a`. At a pole of order `m`, the same calculation gives principal part `-m/(s-a)`.

Therefore the complete list of polar principal parts of `L_f` records precisely:

- the zeros and poles of `f`;
- their multiplicities;
- no holomorphic remainder.

Now suppose `f` and `g` have the same divisor. Their quotient `h=g/f` is holomorphic and zero-free, and

\[
L_g=L_f+\frac{h'}{h}.
\]

The correction `h'/h` is holomorphic, so it changes none of the principal parts. For the elementary family

\[
g_a(s)=e^{as}f(s),
\]

one has the same divisor for every `a`, while

\[
L_{g_a}=L_f+a.
\]

Thus even a constant holomorphic term is already invisible after principal-part compression. On a simply connected domain the freedom is larger: every holomorphic `u` has a primitive `H`, and `h=e^H` gives `h'/h=u`. On a general connected domain the admissible holomorphic defects are exactly logarithmic derivatives of globally defined nowhere-zero holomorphic factors.

The important distinction is therefore not merely

\[
\text{function}\to\text{zeros},
\]

but

\[
\text{exact log derivative}
\to
\text{its polar part}.
\]

The latter map deletes the analytic information carried by the zero-free factor while retaining its divisor contribution exactly.

## Euler-product fidelity

Let `Q={q_j}` satisfy AF-017's local-finiteness and absolute-convergence hypotheses. In the convergence half-plane,

\[
\log Z_Q(s)
=\sum_j\sum_{m\ge1}\frac{q_j^{-ms}}{m},
\]

so termwise differentiation gives

\[
\boxed{
-\frac{Z_Q'(s)}{Z_Q(s)}
=\sum_j\sum_{m\ge1}(\log q_j)q_j^{-ms}.
}
\]

For ordinary rational primes this specializes to the classical von Mangoldt Dirichlet series

\[
-\frac{\zeta'(s)}{\zeta(s)}
=\sum_{n\ge1}\frac{\Lambda(n)}{n^s},
\qquad \Re(s)>1.
\]

Suppose now

\[
\frac{Z_Q'}{Z_Q}=\frac{Z_R'}{Z_R}
\]

on a common connected convergence half-plane. By the exact recovery result above,

\[
Z_Q=CZ_R.
\]

But absolute convergence and `q_j,r_j>1` imply

\[
Z_Q(\sigma)\to1,
\qquad
Z_R(\sigma)\to1
\qquad(\sigma\to+\infty),
\]

so `C=1`. Therefore `Z_Q=Z_R`. AF-017 then recovers equality of the underlying norm multisets:

\[
\boxed{
\frac{Z_Q'}{Z_Q}=\frac{Z_R'}{Z_R}
\Longrightarrow
Q=R
\text{ as multisets}.
}
\]

Thus differentiation has discarded the overall multiplicative normalization of an arbitrary meromorphic function, but the canonical Euler-product normalization restores it for free. In this category the exact logarithmic derivative remains rational-prime-norm faithful whenever the exact Euler product was.

## Grosswald--Schnitzer matched control

AF-017 used Grosswald and Schnitzer's family

\[
\zeta^*=\phi\zeta
\]

with `phi` holomorphic and nowhere zero in `Re(s)>0`. Their modified Euler products can change the generator norms while preserving the zeta zeros with multiplicity and the simple pole at `s=1`.

Taking logarithmic derivatives gives

\[
\frac{\zeta^{*\prime}}{\zeta^*}
=
\frac{\zeta'}{\zeta}
+
\frac{\phi'}{\phi}.
\]

Because `phi'/phi` is holomorphic, it contributes no poles or residues. Therefore any representation that retains only the singular part of the logarithmic derivative sees exactly the same destination for `zeta` and these changed-generator controls.

By contrast, an exact-log-derivative representation sees the holomorphic term unless `phi` is constant. If it were constant while both normalized Euler products tend to one in their convergence half-plane, that constant would be one, forcing equality of the exact Euler products and hence, by AF-017, equality of the norm multisets. A genuinely changed Grosswald--Schnitzer generator system therefore cannot be invisible to the exact logarithmic derivative.

This gives a same-family witness for both sides of the boundary:

\[
\begin{array}{c|c}
\text{retained layer} & \text{Grosswald--Schnitzer control}\\
\hline
\text{exact }Z'/Z & \text{distinguished}\\
\text{poles/residues of }Z'/Z & \text{indistinguishable}
\end{array}
\]

## Relation to AF-017, AF-018, and explicit-formula routes

AF-017 showed that the exact Euler-product function contains the generator-norm multiset while its meromorphic divisor need not. AF-018 then showed that sufficiently rigid independently supplied growth, reflection, and normalization constraints can reconstruct a completed order-one entire function from that divisor.

AF-019 inserts another natural analytic layer between those two viewpoints. The exact logarithmic derivative already quotients out one global scalar, but otherwise remembers every zero-free factor through its logarithmic derivative. Throwing away its holomorphic part and retaining only residues collapses it back to divisor data.

This matters for explicit-formula arguments because logarithmic derivatives are the analytic interface through which Euler factors become prime-power weights and zeros become residues. The words "logarithmic derivative", "explicit formula", and "zero data" must therefore not be treated as one fidelity category. A contour argument may begin from the exact function `-Z'/Z` and later use residues; whether the holomorphic remainder survives that passage is a separate compression question.

The Arithmetic Fidelity audit should distinguish at least:

\[
\text{Euler/local-factor data}
\to
\text{exact log derivative}
\to
\text{contour/transform data}
\to
\text{residue or zero summary}.
\]

A prime-specific mechanism located after the last arrow must justify why discarded holomorphic or boundary terms are irrelevant to the discriminator rather than assuming that the zeros inherited all information present in the exact logarithmic derivative.

## Prior art and novelty assessment

All analytic ingredients are classical.

The local fact that `f'/f` has residue equal to zero multiplicity and minus pole multiplicity is standard logarithmic-residue theory. The implication

\[
\frac{f'}f=\frac{g'}g
\Longrightarrow
\frac gf=\text{constant}
\]

is an elementary consequence. The von Mangoldt Dirichlet series for `-zeta'/zeta` is classical analytic number theory. Grosswald--Schnitzer's modified-zeta factorization is already the prior-art matched control used in AF-017.

No novelty is claimed for any of these identities or recovery facts individually. The Arithmetic Fidelity contribution is the **adjacent-layer placement**: exact logarithmic-derivative data retain the zero-free factor modulo scale and remain generator-norm faithful after Euler normalization, whereas principal-part compression retains precisely the divisor and therefore re-enters the non-faithful Grosswald--Schnitzer layer.

This is a classification of where information is lost, not a new theorem about the zeros of `zeta` and not evidence for RH.

## Boundaries and failure modes

- `Omega` must be connected for the residual quotient to be one global constant rather than one constant per connected component.
- Equality of exact logarithmic derivatives is much stronger than agreement of poles, residues, finitely many values, moments, contour integrals, or asymptotics.
- Principal-part data mean the complete local polar terms with multiplicities. Additional regular values, boundary data, transform values, or normalization constraints define a richer destination and must be audited separately.
- For same-divisor meromorphic functions on a non-simply-connected domain, the holomorphic difference of logarithmic derivatives is constrained by being `h'/h` for a globally defined zero-free `h`; it is not automatically an arbitrary holomorphic function.
- The Euler-product norm-recovery statement inherits AF-017's exact Euler-factor form, local-finiteness, and absolute-convergence assumptions.
- Recovery is only of the unordered generator-norm multiset. It does not recover labels, order, splitting provenance, additive structure, number fields, or other richer arithmetic relations.
- Grosswald--Schnitzer controls establish non-fidelity for divisor/principal-part data in their continuation domain; they do not show that every richer explicit-formula or operator representation is non-faithful.
- A contour integral can retain information through regular terms, boundary terms, test functions, or normalization even when a residue-only summary would not. One must compute the actual destination map rather than infer loss from the presence of residues alone.
- No statement here depends on RH or constrains the location of the nontrivial zeta zeros.

## Decisive audit test

For any RH-relevant route using a logarithmic derivative or explicit formula:

1. state whether the retained object is the exact meromorphic function `Z'/Z`, a transform of it, or only its pole/residue data;
2. compute the full same-destination fiber at that exact layer, including holomorphic zero-free-factor contributions;
3. apply a Grosswald--Schnitzer-type changed-generator control whenever the destination has collapsed to divisor/principal-part information;
4. if the route retains additional regular, boundary, normalization, or transform data, prove which part of `h'/h` those data determine;
5. only then claim rational-prime-norm fidelity, and distinguish recovery of norms from recovery of richer arithmetic provenance.

A same-principal-part control with different generator norms kills prime-norm recovery at that layer. Equality of the exact normalized Euler-product logarithmic derivative does not: it forces equality of the exact Euler product and hence equality of the norm multiset.

## Consequence for the line

Treat the **regular part of a logarithmic derivative** as an explicit fidelity carrier rather than disposable analytic background.

The refined arithmetic chain is now

\[
\boxed{
\text{normed prime system}
\to
\text{exact Euler product}
\to
\text{exact logarithmic derivative}
\to
\text{principal parts/divisor}.
}
\]

Under AF-017's Euler-product hypotheses, the first three layers retain the unordered generator norms; the last one can lose them. Future spectral, explicit-formula, and positivity audits should locate whether their actual compression preserves the regular/zero-free contribution or quotients it away before asking the final representation to distinguish the rational primes.