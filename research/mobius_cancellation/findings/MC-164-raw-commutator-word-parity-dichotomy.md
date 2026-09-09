# MC-164 — Adjoint-free raw prime-commutator words have an exact degree-parity phase dichotomy

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `BOUNDARY/CONDITIONAL-GAIN`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue in the canonical number-state representation used in `MC-149`–`MC-163`,

\[
\mathcal H=\ell^2(\mathbb N),
\qquad
S_p\varepsilon_n=\varepsilon_{pn},
\qquad
D_\mu\varepsilon_n=\mu(n)\varepsilon_n,
\]

and write

\[
C_p:=[D_\mu,S_p].
\tag{1}
\]

`MC-159` left genuinely noncommutative products outside finite joint scalar functional calculus, and `MC-163` then showed that the first quadratic **Gram** relation `C_p^*C_q` reduces to square-free prime-support replacement with factorized endpoint phase. The simplest remaining adjoint-free question is therefore whether ordered products of the raw `C_p` create a new cross-prime Möbius phase.

They do not. They obey an exact degree-parity law.

Let

\[
\mathbf p=(p_1,\ldots,p_r)
\]

be an ordered tuple of distinct primes, let

\[
P_{\mathbf p}:=\prod_{j=1}^r p_j,
\]

and define the raw word, with `p_1` acting first,

\[
W_{\mathbf p}:=C_{p_r}\cdots C_{p_1}.
\tag{2}
\]

Let `P_p=S_pS_p^*` be the divisibility projection and let `P_sf` be the projection onto square-free basis states. Put

\[
\epsilon_r:=(-1)^{r(r+1)/2}
\]

and

\[
Q_{\mathbf p}
:=
P_{\rm sf}
\left(\prod_{j=1}^{r-1}(I-P_{p_j})\right)
(2I-P_{p_r}).
\tag{3}
\]

Then the exact pulled-back operator identity is

\[
\boxed{
S_{P_{\mathbf p}}^*W_{\mathbf p}
=
\epsilon_r\,2^{r-1}D_\mu^{\,r}Q_{\mathbf p}.
}
\tag{4}
\]

Equivalently, if `n` is squarefree and none of `p_1,\ldots,p_{r-1}` divides `n`, then

\[
W_{\mathbf p}\varepsilon_n
=
\begin{cases}
\epsilon_r\,2^r\mu(n)^r\,\varepsilon_{P_{\mathbf p}n},
& p_r\nmid n,\\
\epsilon_r\,2^{r-1}\mu(n)^r\,\varepsilon_{P_{\mathbf p}n},
& p_r\mid n,
\end{cases}
\tag{5}
\]

and the word vanishes on every nonsquarefree `n` and whenever one of `p_1,\ldots,p_{r-1}` already divides `n`.

Since

\[
D_\mu^{2m}=P_{\rm sf},
\qquad
D_\mu^{2m+1}=D_\mu
\qquad(m\ge1),
\tag{6}
\]

equation `(4)` gives the dichotomy:

- every **even-degree** adjoint-free word is completely determined by square-free support and finitely many prime-divisibility projections;
- every **odd-degree** word retains the original Möbius orientation linearly, multiplied only by an explicit support/divisibility mask.

Thus raw noncommutative multiplication does not generate a third, relational phase class between support-only data and the original target orientation. At this monomial level, even degree squares the Möbius phase away; odd degree simply carries it forward.

The first nontrivial Lie-bracket consequence is particularly sharp. For distinct primes `p,q`,

\[
\boxed{
S_{pq}^*[C_p,C_q]
=2P_{\rm sf}(P_q-P_p),
}
\tag{7}
\]

or equivalently

\[
\boxed{
[C_p,C_q]
=2S_{pq}P_{\rm sf}(P_q-P_p).
}
\tag{8}
\]

So the simplest genuinely noncommuting relation among two raw prime channels contains **no Möbius sign coefficient at all**. It records only the oriented divisibility asymmetry “`q` divides but `p` does not” versus “`p` divides but `q` does not”.

This closes the most immediate adjoint-free quadratic escape from `MC-163`. More generally, `(4)` classifies every distinct-prime raw monomial: even words collapse to the support/divisibility algebra, while odd words do not manufacture a new phase coupling but retain the same pointwise orientation already shown target-complete at first order in `MC-156`.

## 1. The one-step coefficient is a local Möbius phase times a divisibility amplitude

For a prime `p`,

\[
C_p\varepsilon_n
=\bigl(\mu(pn)-\mu(n)\bigr)\varepsilon_{pn}.
\tag{9}
\]

If `n` is nonsquarefree, both Möbius values vanish. If `n` is squarefree, then

\[
\mu(pn)-\mu(n)
=
\begin{cases}
-2\mu(n),&p\nmid n,\\
-\mu(n),&p\mid n.
\end{cases}
\tag{10}
\]

Thus a nonzero application of `C_p` contributes one factor of the current square-free Möbius phase. If `p` was absent, the output remains squarefree and the Möbius phase flips; if `p` was already present, the output becomes nonsquarefree and every later raw commutator kills it.

That last observation is the only order dependence needed below.

## 2. Ordered products have an exact closed form

Apply `C_{p_1},C_{p_2},\ldots,C_{p_r}` successively. A nonzero word of length at least two requires

\[
p_j\nmid n
\qquad(1\le j<r),
\tag{11}
\]

because hitting an already-present prime before the final step creates a square factor and forces the remaining word to vanish.

Assume `(11)` and that `n` is squarefree. Before the `j`-th step, for `j<r`, the current state is

\[
n\prod_{i<j}p_i
\]

and its Möbius value is

\[
(-1)^{j-1}\mu(n).
\]

Hence the `j`-th coefficient for `j<r` is

\[
-2(-1)^{j-1}\mu(n)
=2(-1)^j\mu(n).
\tag{12}
\]

At the last step the same coefficient has magnitude `2` if `p_r` was absent from `n` and magnitude `1` if `p_r` was already present. In both cases its sign is `(-1)^r\mu(n)`. Multiplying the `r` factors gives

\[
(-1)^{1+2+\cdots+r}\mu(n)^r
=
\epsilon_r\mu(n)^r
\tag{13}
\]

together with magnitude `2^r` or `2^{r-1}`. This proves `(5)`.

Pulling the common output shift `S_{P_{\mathbf p}}` back to the input basis gives `(4)`: the first `r-1` factors in `(3)` enforce `(11)`, the last factor `2I-P_{p_r}` distinguishes the two allowed final cases, and `P_sf` removes nonsquarefree inputs.

No limiting argument, KMS state, scalar norm, or analytic continuation is involved.

## 3. The phase-deformation family shows why only word parity survives

The matched local-phase family used in `MC-163` makes the mechanism more transparent. For unimodular prime phases `z_p`, define

\[
f_z(n)=
\begin{cases}
\prod_{p\mid n}z_p,&n\text{ squarefree},\\
0,&n\text{ otherwise},
\end{cases}
\qquad
D_z\varepsilon_n=f_z(n)\varepsilon_n,
\]

and

\[
C_p^{(z)}=[D_z,S_p].
\tag{14}
\]

For the same ordered distinct-prime word

\[
W_{\mathbf p}^{(z)}
=C_{p_r}^{(z)}\cdots C_{p_1}^{(z)},
\]

the same support condition `(11)` is necessary. If it holds and `p_r\nmid n`, direct multiplication gives

\[
\boxed{
W_{\mathbf p}^{(z)}\varepsilon_n
=
f_z(n)^r
\left(\prod_{j=1}^r(z_{p_j}-1)\right)
\left(\prod_{j=1}^{r-1}z_{p_j}^{\,r-j}\right)
\varepsilon_{P_{\mathbf p}n}.
}
\tag{15}
\]

If instead `p_r\mid n`, the final finite difference is the squareful boundary term and

\[
\boxed{
W_{\mathbf p}^{(z)}\varepsilon_n
=
-f_z(n)^r
\left(\prod_{j=1}^{r-1}(z_{p_j}-1)\right)
\left(\prod_{j=1}^{r-1}z_{p_j}^{\,r-j}\right)
\varepsilon_{P_{\mathbf p}n}.
}
\tag{16}
\]

All cross-prime phase dependence therefore separates into a power `f_z(n)^r` of the original state phase and a product of one-prime factors. There is no new pairwise or higher interaction phase created by the raw word itself.

At the Möbius specialization `z_p=-1`, one has `f_z(n)=\mu(n)` on the square-free sector. Because that local phase has order two, `(15)`–`(16)` collapse exactly according to the parity of `r`. The even sector forgets state orientation; the odd sector returns the original orientation.

This is the adjoint-free counterpart of the Gram factorization in `MC-163`: there the conjugate pairing cancels the accumulated state phase at quadratic order, whereas here ordinary multiplication raises it to the word degree.

## 4. The raw two-channel Lie bracket is purely support/divisibility data

Take `r=2`. Equation `(4)` gives

\[
S_{pq}^*C_qC_p
=-2P_{\rm sf}(I-P_p)(2I-P_q),
\tag{17}
\]

and, reversing the order,

\[
S_{pq}^*C_pC_q
=-2P_{\rm sf}(I-P_q)(2I-P_p).
\tag{18}
\]

Subtracting `(17)` from `(18)` yields `(7)`. On a square-free basis state this means

\[
[C_p,C_q]\varepsilon_n
=
\begin{cases}
-2\varepsilon_{pqn},&p\mid n,\ q\nmid n,\\
+2\varepsilon_{pqn},&q\mid n,\ p\nmid n,\\
0,&\text{otherwise}.
\end{cases}
\tag{19}
\]

The coefficient is independent of `\mu(n)`. Its polar data, norm, absolute value, and every scalar functional of the pulled-back diagonal `(7)` therefore live entirely in the square-free/divisibility algebra.

This is stronger than saying that a norm loses one sign: the full raw bracket operator itself has already eliminated the Möbius orientation before any external scalarization.

## 5. Odd raw words retain rather than explain the target phase

For odd `r`, equation `(4)` becomes

\[
S_{P_{\mathbf p}}^*W_{\mathbf p}
=
\epsilon_r2^{r-1}D_\mu Q_{\mathbf p}.
\tag{20}
\]

Thus wherever the explicit support mask `Q_{\mathbf p}` is nonzero, the sign of the word coefficient is exactly the sign of `\mu(n)` up to the known constant `\epsilon_r`.

A single fixed odd word does not see states divisible by one of its first `r-1` primes. But the full family is pointwise target-complete: for every square-free `n`, choose the first `r-1` primes outside the finite support of `n`. Then `(20)` reads `\mu(n)` directly from that word coefficient; nonsquarefree states are already identified by the common zero support.

This does not supply a Mertens estimate. It identifies an information boundary. Odd-degree raw words have not compressed the difficult orientation into a new easier invariant; they retain a masked copy of the same pointwise sign field. In fact the degree-one case is the already stronger statement `MC-156`, where one fixed prime commutator's complete signed coefficient table cubically reconstructs `D_\mu` everywhere.

Hence increasing the raw noncommutative word length does not repair the two-sided failure exposed by the earlier commutator findings:

- even degree throws away the orientation needed by `M(x)`;
- odd degree keeps that orientation rather than deriving a cheaper cancellation law from it.

## 6. Prior-art and novelty audit

The Bost–Connes system, its canonical multiplicative semigroup isometries, and the relevant number-state representation are established prior art already audited in `MC-138`–`MC-163`. `MC-163` records the primary Bost–Connes reference (Bost–Connes, *Selecta Mathematica* 1995), Laca's semigroup-dilation/corner framework, and Greenfield–Marcolli–Teh's twisted-spectral-triple work as the nearby noncommutative-geometry boundary.

Products of weighted shifts and elementary commutator identities are standard operator theory. A targeted literature search around Bost–Connes semigroup commutators, iterated/raw commutator products, Möbius diagonals, and prime isometries did not locate this exact degree-parity specialization. That search absence is not used as novelty evidence. Equations `(4)` and `(15)`–`(16)` are elementary consequences of the canonical represented action and the square-free multiplicative phase law, so the finding makes **no novelty claim**.

The substantive line-level delta is narrower: `MC-163` deliberately left unmatched adjoint-free words outside its Gram theorem. The present exact classification closes all distinct-prime adjoint-free monomials at once and identifies the simplest Lie bracket `(7)` as support-only.

## Boundaries and falsification tests

- **Distinct primes.** Equations `(3)`–`(5)` assume the primes in the word are distinct. Repeated-prime words encounter squareful states at different positions and require a separate classification. They do not invalidate the stated distinct-prime theorem.
- **Adjoint-free monomials only.** Mixed words containing both `C_p` and `C_q^*`, coefficient-algebra insertions, twisted commutators, resolvents, or other source-defined operations are outside `(4)`. `MC-163` covers the specific quadratic Gram family `C_p^*C_q`, not all such mixed words.
- **Linear combinations can mix parity sectors.** An arbitrary noncommutative polynomial combining even and odd degrees can contain a support baseline plus masked copies of `D_\mu`. It requires its own cancellation-transfer and reconstruction audit; the present theorem does not claim every polynomial is either globally support-only or globally invertible.
- **Support is not an independent arithmetic universe.** For the actual Möbius function, square-free support together with prime factorization already determines `(-1)^{\omega(n)}`. “Support-only” here means that the represented coefficient in the classified even word contains no additional Möbius orientation beyond square-free/divisibility data; it is not a claim that an omniscient observer cannot reconstruct Möbius from integer factorization.
- **Odd-sector retention is not a cancellation estimate.** Pointwise access to `D_\mu` is target completeness, not evidence of a source-side bound for its additive partial sums.
- **The phase-deformation family is a diagnostic matched control.** It isolates whether a proposed raw word creates genuinely joint phase dependence. It is not assumed to satisfy every arithmetic theorem special to rational-prime Möbius.
- **No RH input.** The calculation uses only the exact local Möbius transition law and the canonical semigroup action. No contour shift, zero-free region, explicit formula, or RH-equivalent bound enters.
- **Direct falsification.** A counterexample consists of one ordered distinct-prime tuple and one basis state violating `(4)` or, in the phase family, `(15)`–`(16)`. The case split above exhausts square-free and squareful inputs.

## Consequence for the line

The residual Bost–Connes/semigroup frontier after `MC-163` should no longer list plain adjoint-free products or the raw two-channel Lie bracket as plausible sources of a new cross-prime Möbius phase. Their exact algebra is now classified: the phase carried by a degree-`r` word is the original state phase raised to degree `r`, times separable local prime factors and a support mask.

A surviving genuinely relational route must therefore alter this factorization rather than merely increase word length. Natural possibilities still outside the theorem include coefficient-algebra insertions between commutators, source-forced twists that change the phase transport law, mixed adjoint/non-adjoint words beyond the Gram family, or state-to-state/scale couplings whose quantitative estimate does not reduce either to square-free support or to a masked reconstruction of `D_\mu`. Any such candidate must still pass the line's target-reencoding and Mertens-transfer tests.