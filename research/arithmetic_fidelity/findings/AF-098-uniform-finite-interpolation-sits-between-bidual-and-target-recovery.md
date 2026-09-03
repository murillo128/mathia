# AF-098 — Uniform finite interpolation sits between bidual and target recovery

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `QUANTITATIVE-FIDELITY-REFINEMENT`, `CLASSICAL-COMPACTNESS-MECHANISM`, `NO-NOVELTY-CLAIM`

## Claim

Let `Z` be a closed linear subspace of a Banach space `X`, let `K` be a Banach space, and let

\[
T\in\mathcal L(Z,K).
\tag{1}
\]

AF-097 showed that every finite-dimensional restriction of `T` extends to `X`, even when `T` itself does not. The missing datum is therefore not finite exact solvability but **uniform conditioning of those finite repairs**.

For every finite-dimensional `E\subset Z`, define the exact interpolation cost

\[
e_E(T)
:=
\inf\{\|S\|:S\in\mathcal L(X,K),\ S|_E=T|_E\},
\tag{2}
\]

and define three recovery costs, with the convention that an infimum over an empty set is `+\infty`:

\[
\lambda_{**}(T)
:=
\inf\{\|U\|:U\in\mathcal L(X,K^{**}),\ U|_Z=J_KT\},
\tag{3}
\]

\[
\lambda_{\rm fin}(T)
:=
\sup_{\substack{E\subset Z\\\dim E<\infty}} e_E(T),
\tag{4}
\]

and

\[
\lambda_K(T)
:=
\inf\{\|S\|:S\in\mathcal L(X,K),\ S|_Z=T\}.
\tag{5}
\]

Here `J_K:K\to K^{**}` is the canonical embedding. Then:

1. **Finite exact interpolation is always possible, but its worst conditioning can diverge.** If `n=\dim E`, AF-097 gives

   \[
   e_E(T)\le n\|T\|.
   \tag{6}
   \]

   Moreover

   \[
   \boxed{\|T\|\le\lambda_{\rm fin}(T)\le\lambda_K(T).}
   \tag{7}
   \]

2. **Uniform finite conditioning forces a genuine global recovery after canonical bidual relaxation.** One always has

   \[
   \boxed{
   \lambda_{**}(T)
   \le
   \lambda_{\rm fin}(T)
   \le
   \lambda_K(T).
   }
   \tag{8}
   \]

   In particular, if `\lambda_{\rm fin}(T)<\infty`, there exists one bounded operator

   \[
   U:X\to K^{**},
   \qquad
   U|_Z=J_KT,
   \qquad
   \|U\|\le\lambda_{\rm fin}(T).
   \tag{9}
   \]

   Thus a family of unrelated finite repairs whose norms remain uniformly bounded cannot remain merely local: compactness forces them to cohere into a bidual-valued global repair.

3. **Complementability of the target in its bidual controls the remaining range loss.** Suppose there is a bounded linear retraction

   \[
   Q:K^{**}\to K,
   \qquad
   QJ_K=I_K,
   \qquad
   \|Q\|\le p.
   \tag{10}
   \]

   Then

   \[
   \boxed{
   \lambda_{**}(T)
   \le
   \lambda_{\rm fin}(T)
   \le
   \lambda_K(T)
   \le
   p\,\lambda_{**}(T).
   }
   \tag{11}
   \]

   Hence all three costs are equivalent up to the bidual projection constant. If `p=1`, they coincide exactly:

   \[
   \boxed{
   \lambda_{**}(T)
   =
   \lambda_{\rm fin}(T)
   =
   \lambda_K(T).
   }
   \tag{12}
   \]

4. **Dual and reflexive targets close the finite-to-global gap with no loss.** If `K=Y^*` is given as a dual Banach space, then

   \[
   J_Y^*:Y^{***}=K^{**}\to Y^*=K
   \tag{13}
   \]

   is a norm-one retraction of `J_K`. Reflexive `K` is the special case in which `J_K` is onto. Therefore (12) holds for every dual or reflexive target.

5. **A fixed norm budget restores finite falsifiability in the dual-target category.** For `n\ge1` define

   \[
   g_T(n)
   :=
   \sup_{\substack{E\subset Z\\1\le\dim E\le n}} e_E(T).
   \tag{14}
   \]

   Then `g_T(n)` is nondecreasing,

   \[
   g_T(n)\le n\|T\|,
   \qquad
   \sup_n g_T(n)=\lambda_{\rm fin}(T).
   \tag{15}
   \]

   If `K` is `1`-complemented in `K^{**}` -- in particular if `K` is dual or reflexive -- then

   \[
   \boxed{
   T\text{ extends boundedly to }X
   \iff
   \sup_n g_T(n)<\infty,
   }
   \tag{16}
   \]

   and the least global extension norm is exactly `\sup_n g_T(n)`. Equivalently, whenever

   \[
   C<\lambda_K(T),
   \tag{17}
   \]

   there is a finite-dimensional `E\subset Z` such that **every** exact interpolant `S:X\to K` satisfying `S|_E=T|_E` has

   \[
   \|S\|>C.
   \tag{18}
   \]

   If no global extension exists, such a finite witness exists for every finite budget `C`, and `g_T(n)\to\infty`.

The reusable Arithmetic Fidelity boundary is therefore

\[
\boxed{
\text{finite point values do not detect extension, but finite point values plus a uniform conditioning budget can.}
}
\tag{19}
\]

AF-097's pointwise invisibility is not contradicted: without a norm budget, every finite restriction is exactly reproducible. The new discriminator is the **growth of the cost required to keep those finite reproductions globally bounded on the source space**.

## Derivation

### 1. Finite interpolation costs are finite and recover `\|T\|` in the limit

AF-097 gives, for each finite-dimensional `E\subset Z` of dimension `n`, an extension `S_E:X\to K` satisfying

\[
S_E|_E=T|_E,
\qquad
\|S_E\|\le n\|T\|.
\tag{20}
\]

Thus `e_E(T)<\infty` and (6) holds. Every global extension of `T` is an admissible interpolant for every `E`, so

\[
e_E(T)\le\lambda_K(T)
\tag{21}
\]

for all finite `E`, proving the right inequality in (7).

Conversely `e_E(T)\ge\|T|_E\|`. Taking one-dimensional subspaces through vectors on which `T` approaches its norm gives

\[
\sup_{\dim E<\infty}\|T|_E\|=\|T\|,
\tag{22}
\]

so `\lambda_{\rm fin}(T)\ge\|T\|`.

### 2. Compactness turns uniform finite repairs into one bidual extension

Assume

\[
c:=\lambda_{\rm fin}(T)<\infty.
\tag{23}
\]

Fix `C>c`. Consider the set

\[
\Omega_C
:=
\{U\in\mathcal L(X,K^{**}):\|U\|\le C\}
\tag{24}
\]

with the topology of pointwise weak-star convergence `\sigma(K^{**},K^*)`. It is compact. Indeed, it is a closed subset of

\[
\prod_{x\in X} C\|x\|B_{K^{**}},
\tag{25}
\]

which is compact by Banach--Alaoglu and Tychonoff; linearity is closed under pointwise weak-star limits.

For each finite-dimensional `E\subset Z`, let

\[
A_E
:=
\{U\in\Omega_C:U|_E=J_KT|_E\}.
\tag{26}
\]

Each `A_E` is closed. The family `(A_E)` has the finite-intersection property. Given finitely many `E_1,\ldots,E_m`, put

\[
E=E_1+\cdots+E_m.
\tag{27}
\]

Since `e_E(T)\le c<C`, there exists `S\in\mathcal L(X,K)` with

\[
S|_E=T|_E,
\qquad
\|S\|<C.
\tag{28}
\]

Then `J_KS\in A_{E_1}\cap\cdots\cap A_{E_m}`. Compactness therefore gives

\[
\bigcap_{\dim E<\infty}A_E\ne\varnothing.
\tag{29}
\]

Any element `U_C` of this intersection extends `J_KT` to all of `X` and has norm at most `C`.

To remove the arbitrary slack, take `C_m=c+1/m`. Inside the compact set `\Omega_{c+1}`, the nonempty sets

\[
B_m
:=
\{U\in\mathcal L(X,K^{**}):U|_Z=J_KT,\ \|U\|\le c+1/m\}
\tag{30}
\]

are closed and nested. Their intersection contains an extension with norm at most `c`. This proves (9), hence

\[
\lambda_{**}(T)\le\lambda_{\rm fin}(T).
\tag{31}
\]

The second inequality in (8) was already (21).

### 3. A bidual retraction measures exactly how much range fidelity is missing

Assume (10). For every `U:X\to K^{**}` extending `J_KT`, the composition

\[
S:=QU:X\to K
\tag{32}
\]

satisfies

\[
S|_Z=QJ_KT=T
\tag{33}
\]

and

\[
\|S\|\le p\|U\|.
\tag{34}
\]

Taking the infimum over all bidual extensions gives

\[
\lambda_K(T)\le p\lambda_{**}(T),
\tag{35}
\]

which combined with (8) proves (11). When `p=1`, every inequality in (11) must be equality.

For `K=Y^*`, the canonical map `J_Y^*:Y^{***}\to Y^*` has norm one and satisfies

\[
J_Y^*J_{Y^*}=I_{Y^*},
\tag{36}
\]

so the dual-target assertion follows without reflexivity or separability.

### 4. The interpolation profile is the finite certificate once a budget is declared

The monotonicity of `g_T` is immediate from (14). Equation (6) gives its linear upper bound in (15), while every finite-dimensional `E` occurs in some dimension level, so

\[
\sup_n g_T(n)=\lambda_{\rm fin}(T).
\tag{37}
\]

Suppose now that `K` is `1`-complemented in `K^{**}`. Equation (12) gives

\[
\lambda_K(T)=\sup_n g_T(n).
\tag{38}
\]

If `C<\lambda_K(T)`, then `C<\lambda_{\rm fin}(T)`. By the definition of a supremum there is some finite-dimensional `E\subset Z` with

\[
e_E(T)>C,
\tag{39}
\]

which is exactly (18).

This is the precise way in which a quantitative admissibility constraint changes AF-097. The finite observation values still agree perfectly with those of some extendable operator. What eventually fails is the possibility of doing so while keeping the ambient operator norm below one fixed budget.

## Exact controls

### Scalar Hahn--Banach control

For `K=\mathbb R` or `\mathbb C`, Hahn--Banach gives a global norm-preserving extension of every `T\in Z^*`. Hence

\[
\lambda_{**}(T)
=
\lambda_{\rm fin}(T)
=
\lambda_K(T)
=
\|T\|.
\tag{40}
\]

The finite interpolation profile is constant and contains no hidden obstruction.

### Uncomplemented dual-subspace control

Let `Z\subset X` be a closed, uncomplemented subspace which, as a Banach space, is a dual space, and take

\[
K=Z,
\qquad
T=I_Z.
\tag{41}
\]

A global extension `S:X\to Z` of `I_Z` would be a bounded projection onto `Z`, so none exists. Since `K` is dual, (16) forces

\[
\lambda_{\rm fin}(I_Z)=\infty.
\tag{42}
\]

Thus for every `C<\infty` some finite-dimensional `E\subset Z` cannot be fixed by any global map `S:X\to Z` of norm at most `C`, even though AF-097 guarantees that `E` can always be fixed by some bounded global map. This is an exact matched control separating **finite solvability** from **uniform finite solvability**.

### Non-complemented-in-bidual target

For a general `K`, (8) is intentionally one-sided. A bidual-valued extension need not have its range in `J_K(K)`, and no bounded retraction `K^{**}\to K` need exist. Therefore

\[
\lambda_{**}(T)<\infty
\tag{43}
\]

alone does not justify either `\lambda_{\rm fin}(T)<\infty` or a `K`-valued global extension.

The surviving gap is a genuine **range-retention problem**: compactness can close coherence in the canonical bidual while still forgetting membership in the original target category.

### Distinction from classical local complementation

The finite test in (2) must not be conflated with the standard definition of local complementation. Here each interpolant

\[
S_E:X\to K
\tag{44}
\]

is defined on the **whole ambient source `X`** and is required to agree with one fixed operator `T` only on `E\subset Z`. Classical local complementation instead uses uniformly bounded retractions defined on finite-dimensional ambient subspaces `F\subset X` and fixes `F\cap Z`.

The mechanisms are adjacent -- both expose whether finite compatibility can be made uniform -- but the quantifiers and operator spaces are different.

### Barycentric-kernel specialization

For

\[
Z=Z_F\subset\mathcal F(F)
\tag{45}
\]

from AF-093--AF-097, a dual coefficient `K=Y^*` is already in AF-096's ultrasummand regime, so every fiber operator extends globally. AF-098 adds a quantitative statement rather than reopening that defect:

\[
\boxed{
\text{optimal global extension cost}
=
\text{worst finite exact interpolation cost}.
}
\tag{46}
\]

For a genuinely non-ultrasummand coefficient, AF-095 may still allow a robust extension defect. AF-098 now splits that frontier: if a candidate `T` does not even extend into `K^{**}`, then `g_T(n)` must diverge, so the global obstruction appears as arbitrarily bad finite conditioning. If a bidual extension exists while `K`-valued recovery fails, the obstruction lies instead in retaining the original target range and cannot be diagnosed merely from bidual coherence.

## Prior art and novelty assessment

The compactness and Banach-space mechanisms used here are classical. **No novelty is claimed** for Banach--Alaoglu, Tychonoff compactness, bidual embeddings, dual-space retractions, finite-dimensional Hahn--Banach interpolation, local complementation, or compactness arguments turning uniformly bounded local data into global operators.

- Leonidas Alaoglu, **“Weak Topologies of Normed Linear Spaces,”** *Annals of Mathematics* 41(1) (1940), 252--267, DOI `10.2307/1968829`. Role: weak-star compactness of bounded dual balls, which is the compactness input in (24)--(30).
- Nigel J. Kalton, **“Locally Complemented Subspaces and `\mathcal L_p`-Spaces for `0<p<1`,”** *Mathematische Nachrichten* 115(1) (1984), 71--97, DOI `10.1002/mana.19841150107`. Theorem 3.5 records the classical Banach-space equivalence between local complementation, bidual complementation, and a dual extension operator; the preceding Theorem 3.4 explicitly describes its extension step as a “Lindenstrauss compactness argument.” This is the closest classical mechanism boundary, although AF-098's fixed-operator/global-domain interpolation profile has different quantifiers from local complementation.
- Antonio Avilés, Gonzalo Martínez-Cervantes, and Abraham Rueda Zoca, **“Local complementation in Banach spaces and its preservation under free constructions,”** *Quaestiones Mathematicae* 48(2) (2025), 287--298, DOI `10.2989/16073606.2024.2393682`. Role: modern treatment of equivalent local-complementation formulations and preservation under free constructions; it marks the established finite-to-global Banach-space neighborhood surrounding the present specialization.
- AF-089 is the immediate Mathia-local compactness precedent: finite compatibility inside compact admissible fibers globalizes exactly. AF-097 is the immediate obstruction being refined: without uniform norm control, every finite pointwise observation is exactly reproducible by an extendable operator.

A targeted prior-art audit around local complementation, compact extension arguments, dual-valued operator extension, and finite-dimensional interpolation found the classical ingredients and stronger neighboring categorical theories, not a reason to claim a new Banach-space theorem. The durable Arithmetic Fidelity value is the **three-cost classification** (8)--(12) and the resulting audit rule: after pointwise finite tests have become vacuous, track the dimension-dependent conditioning of exact repairs; bounded conditioning forces bidual coherence, while target-bidual complementability decides whether that coherence returns to the original category.

## Boundaries and failure modes

- `\lambda_{\rm fin}` measures exact interpolation by operators defined on all of `X`; it is not the standard local-complementation constant.
- The theorem does not claim `\lambda_{**}=\lambda_{\rm fin}` for arbitrary `K`. The bidual extension produced from finite repairs may exist at lower cost than any uniformly coherent family of `K`-valued finite interpolants.
- The theorem does not claim `\lambda_{\rm fin}=\lambda_K` when `K` is not `1`-complemented in `K^{**}`. A bidual range can carry coherent recovery while the original target range remains inaccessible.
- Equation (6) is only the universal elementary bound from AF-097. No sharp dimension growth is asserted.
- The uncomplemented-dual control is existential at the level of an inclusion `Z\subset X`; it is not a claim that every dual subspace is uncomplemented or that one fixed classical pair realizes every growth pattern.
- A bounded interpolation profile says nothing by itself about canonicity, equivariance, positivity, locality, arithmetic provenance, computability, or another source-specific admissibility requirement.
- No rational-prime specificity or RH conclusion follows.

## Consequences for Arithmetic Fidelity

AF-095 converted robust nonextension into norm-continuous dual witnessability. AF-097 then showed that finite point evaluations cannot see that global defect at all. AF-098 identifies the first quantitative refinement that can escape this blindness without inventing a new observable after the fact: retain not only whether finite data can be matched, but **how the minimal ambient repair cost scales as more source directions are required simultaneously**.

The resulting hierarchy is

\[
\boxed{
\text{finite exact matching}
\;\subset\;
\text{uniformly conditioned finite matching}
\;\Longrightarrow\;
\text{bidual global recovery}
\;\xrightarrow[\text{range gate}]{K^{**}\to K}\;
\text{target-valued global recovery}.
}
\tag{47}
\]

For dual/reflexive targets the range gate is norm-one and the middle stages collapse exactly; global nonextension is then equivalent to divergence of finite interpolation cost. For a noncomplemented target the gap between bidual coherence and target-valued recovery remains live.

This gives a sharper general prescription for later arithmetic applications. Once a compression has erased a discriminator from all finite pointwise tests, a candidate rescue should not merely add more finite samples. It should identify an intrinsic **uniformity/coercivity principle** controlling the cost of making those local repairs compatible, and then justify why the resulting coherent object remains in the intended arithmetic category rather than only in a completion or bidual.