# AF-517 — PNT density governs the partial proportional-tail curvature gap

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `QUANTITATIVE-SEPARATION` · `DIRICHLET-SOURCE` · `PARTIAL-TAIL-DILATION` · `DENSITY-THRESHOLD` · `MESOSCOPIC-BOUNDARY-SCALE` · `NO-NOVELTY-CLAIM`

## Claim

Let

\[
P(s)=\sum_{p\in\mathbb P}p^{-s},
\qquad
\kappa_P(s)=\frac{d^2}{ds^2}\log P(s),
\qquad s>1.
\]

Let `E` be a fixed subset of the rational primes satisfying the prime-number-theorem density condition

\[
\pi_E(x)
:=\#\{p\le x:p\in E\}
=
\delta\,\frac{x}{\log x}
+o\!\left(\frac{x}{\log x}\right)
\qquad (x\to\infty)
\tag{1}
\]

for some `0\le\delta\le1`.

Fix an integer `c\ge2`. For a cutoff `A`, leave every prime outside the selected tail unchanged and replace each selected prime `p>A`, `p\in E`, by the composite atom `cp`:

\[
R_{A,E,c}
=
\bigl(\mathbb P\setminus\{p>A:p\in E\}\bigr)
\cup
\{cp:p>A,\ p\in E\}.
\tag{2}
\]

The atoms in `(2)` are pairwise distinct: moved atoms are composite and therefore cannot collide with an unmoved prime, while `p\mapsto cp` is injective. Define

\[
Q_{A,E,c}(s)
=
\sum_{q\in R_{A,E,c}}q^{-s},
\qquad
\kappa_{A,E,c}(s)
=
\frac{d^2}{ds^2}\log Q_{A,E,c}(s).
\tag{3}
\]

For every fixed `k>1`, set

\[
L=\log A,
\qquad
\ell=\log L,
\qquad
t_A=L^{-k},
\qquad
s_A=1+t_A.
\tag{4}
\]

Put

\[
r
=
\delta\left(1-\frac1c\right)
=
\delta\frac{c-1}{c}.
\tag{5}
\]

Then

\[
\boxed{
\frac{\kappa_{A,E,c}(s_A)}{\kappa_P(s_A)}
\longrightarrow
\frac{k(1-r)}{k-r(k-1)}
}
\tag{6}
\]

and hence

\[
\boxed{
\frac{\kappa_{A,E,c}(s_A)-\kappa_P(s_A)}
{\kappa_P(s_A)}
\longrightarrow
-\frac{r}{k-r(k-1)}.
}
\tag{7}
\]

Thus every fixed positive PNT density `\delta>0` leaves a nonzero mesoscopic curvature witness under a coherent proportional displacement. If `\delta=0`, this particular cutoff-adapted witness vanishes to first order:

\[
\frac{\kappa_{A,E,c}(s_A)}{\kappa_P(s_A)}\longrightarrow1.
\tag{8}
\]

The density law continuously interpolates between no selected tail and AF-515's cofinite proportional dilation. At `\delta=1`, `(7)` becomes

\[
-\frac{c-1}{k+c-1},
\tag{9}
\]

exactly the AF-515 limit.

A concrete unconditional family is obtained by fixing a modulus `m` and a union `B` of reduced residue classes modulo `m`, then taking

\[
E=\{p\in\mathbb P:p\bmod m\in B\}.
\tag{10}
\]

The prime number theorem for arithmetic progressions gives

\[
\delta=\frac{|B|}{\varphi(m)},
\tag{11}
\]

so every nonempty fixed proper union of reduced residue classes gives a genuinely partial, positive-density, all-composite moved tail with the explicit nonzero gap `(7)`.

## Derivation

### 1. PNT density transfers to the first three logarithmic moments

Write

\[
P_E(s)=\sum_{p\in E}p^{-s}.
\tag{12}
\]

Condition `(1)` and partial summation give the standard Abelian boundary asymptotics, as `t\downarrow0`,

\[
P_E(1+t)
=
\delta\log\frac1t
+o\!\left(\log\frac1t\right),
\tag{13}
\]

\[
P_E'(1+t)
=
-\frac{\delta}{t}
+o\!\left(\frac1t\right),
\tag{14}
\]

and

\[
P_E''(1+t)
=
\frac{\delta}{t^2}
+o\!\left(\frac1{t^2}\right).
\tag{15}
\]

For `\delta=0`, the same statements mean `o(log(1/t))`, `o(t^{-1})`, and `o(t^{-2})` respectively. These follow directly from `(1)`; no distribution hypothesis stronger than the stated PNT-density asymptotic is used.

At the cutoff, let

\[
S_{E,A}(s)=\sum_{\substack{p\le A\\p\in E}}p^{-s},
\qquad
T_{E,A}(s)=P_E(s)-S_{E,A}(s).
\tag{16}
\]

The same partial-summation calculation at `x=A` gives

\[
\sum_{\substack{p\le A\\p\in E}}\frac1p
=
\delta\ell+o(\ell),
\tag{17}
\]

\[
\sum_{\substack{p\le A\\p\in E}}\frac{\log p}{p}
=O(L),
\qquad
\sum_{\substack{p\le A\\p\in E}}\frac{(\log p)^2}{p}
=O(L^2).
\tag{18}
\]

Since `t_A L=L^{1-k}\to0`, replacing `p^{-1}` by `p^{-1-t_A}` changes `(17)` by `o(1)`. Therefore

\[
S_{E,A}(s_A)
=
\delta\ell+o(\ell),
\tag{19}
\]

while

\[
S_{E,A}'(s_A)=O(L),
\qquad
S_{E,A}''(s_A)=O(L^2).
\tag{20}
\]

Using `\log(1/t_A)=k\ell`, equations `(13)`--`(20)` imply

\[
T_{E,A}(s_A)
=
\delta(k-1)\ell+o(\ell),
\tag{21}
\]

\[
T_{E,A}'(s_A)
=
-\delta t_A^{-1}+o(t_A^{-1}),
\tag{22}
\]

and

\[
T_{E,A}''(s_A)
=
\delta t_A^{-2}+o(t_A^{-2}),
\tag{23}
\]

because `L=o(L^k)` and `L^2=o(L^{2k})` for `k>1`.

### 2. Partial dilation has an exact one-parameter leading response

The transformed source can be written exactly as

\[
Q_{A,E,c}(s)
=
P(s)+\bigl(c^{-s}-1\bigr)T_{E,A}(s).
\tag{24}
\]

Let

\[
a(s)=c^{-s},
\qquad
b(s)=1-a(s).
\tag{25}
\]

Then `b(s_A)\to(c-1)/c`, and `(24)` becomes

\[
Q_{A,E,c}=P-bT_{E,A}.
\tag{26}
\]

AF-515 gives the prime-source scale

\[
P(s_A)=k\ell+O(1),
\qquad
P'(s_A)=-t_A^{-1}+o(t_A^{-1}),
\qquad
P''(s_A)=t_A^{-2}+o(t_A^{-2}).
\tag{27}
\]

Combining `(21)`, `(26)`, and `(27)` yields

\[
Q_{A,E,c}(s_A)
=
\bigl(k-r(k-1)\bigr)\ell+o(\ell).
\tag{28}
\]

Set

\[
D=k-r(k-1).
\tag{29}
\]

Because `0\le r<1`, one has `D>1`, so the transformed source stays on a positive logarithmic scale.

Differentiate `(26)`:

\[
Q'
=
P'-b'T_{E,A}-bT_{E,A}',
\tag{30}
\]

\[
Q''
=
P''-b''T_{E,A}-2b'T_{E,A}'-bT_{E,A}''.
\tag{31}
\]

The derivatives `b'` and `b''` remain bounded near `s=1`. Hence `(21)`--`(23)` show that the terms containing `b'` or `b''` are lower order than the leading derivative scales. Therefore

\[
Q_{A,E,c}'(s_A)
=
-(1-r)t_A^{-1}+o(t_A^{-1}),
\tag{32}
\]

and

\[
Q_{A,E,c}''(s_A)
=
(1-r)t_A^{-2}+o(t_A^{-2}).
\tag{33}
\]

### 3. The logarithmic curvature reads the selected-tail density

From `(28)`, `(32)`, and `(33)`,

\[
\frac{Q''}{Q}(s_A)
\sim
\frac{1-r}{D}\frac{t_A^{-2}}{\ell}.
\tag{34}
\]

Meanwhile

\[
\left(\frac{Q'}{Q}\right)^2(s_A)
=
O\!\left(\frac{t_A^{-2}}{\ell^2}\right),
\tag{35}
\]

which is lower by one factor of `\ell`. Consequently

\[
\kappa_{A,E,c}(s_A)
\sim
\frac{1-r}{D}\frac{t_A^{-2}}{\ell}.
\tag{36}
\]

The corresponding prime curvature satisfies

\[
\kappa_P(s_A)
\sim
\frac1k\frac{t_A^{-2}}{\ell}.
\tag{37}
\]

Dividing `(36)` by `(37)` proves `(6)`. Subtracting one gives

\[
\frac{k(1-r)}{D}-1
=
\frac{k(1-r)-\bigl(k-r(k-1)\bigr)}{D}
=
-\frac rD,
\tag{38}
\]

which proves `(7)`.

### 4. Fixed arithmetic progressions supply exact positive-density controls

For a fixed modulus `m` and a union `B` of reduced residue classes, the classical prime number theorem for arithmetic progressions gives

\[
\pi_E(x)
=
\frac{|B|}{\varphi(m)}\frac{x}{\log x}
+o\!\left(\frac{x}{\log x}\right).
\tag{39}
\]

Thus `(1)` holds with `(11)`, and the full theorem applies.

For integer `c\ge2`, every moved atom `cp` is composite. Therefore this is an ordinary-integer matched control that changes only a prescribed positive-density subfamily of the prime tail while leaving all other primes untouched.

## Fidelity and matched-control audit

AF-515 showed that moving the entire tail onto a different dilation gauge creates a fixed mesoscopic curvature defect. AF-516 showed that this witness survives uniformly sublinear rounding around that proportional ray. AF-517 identifies a separate resource controlling **how much of the tail must participate**.

Within the PNT-regular class `(1)`, the leading defect depends on the selected set only through

\[
r=\delta\frac{c-1}{c}.
\tag{40}
\]

The response is strictly nonzero for every fixed `\delta>0` and tends continuously to zero with `\delta`. For small density,

\[
\frac{r}{k-r(k-1)}
=
\frac{\delta(c-1)}{ck}
+O(\delta^2).
\tag{41}
\]

Hence there is no positive-density phase transition hidden inside this family: every fixed positive PNT density remains visible, but with a gap proportional to density at first order.

The `\delta=0` case is equally informative. A PNT-regular thinning set contributes only lower-order mass to the value and first two logarithmic moments, so the AF-515 interface mechanism disappears at the scale `(4)`. This does **not** prove that every zero-density or sparse proportional transport is invisible. It says that any surviving witness must come from finer distributional structure than a nonzero PNT-density coefficient.

## Representation audit

The representation remains the relative log-curvature carrier

\[
\|Q-\mathbb P\|_{\mathrm{rel}\,\kappa}
=
\sup_{s>1}
\frac{|\kappa_Q(s)-\kappa_P(s)|}{\kappa_P(s)}.
\tag{42}
\]

No mark or side channel is added. The new result identifies one statistic of the source perturbation that survives this compression at the cutoff-adapted boundary scale: the leading PNT density of a coherently dilated tail subset.

This also sharpens what `sparse` must mean in the next transport audit. Fixed positive prime density is not sparse enough to erase the proportional-interface witness. The unresolved regime is controlled by finer scale-dependent density: zero-density sets, long blocks and gaps, oscillatory selections, or subsets whose effective density depends on the same Laplace scale `t_A` used by the curvature probe.

## Prior art and novelty assessment

No novelty is claimed for the analytic-number-theory ingredients.

- C.-E. Fröberg, **“On the prime zeta function,”** *BIT* 8 (1968), 187–202, DOI `10.1007/BF01933420`, is the classical source for prime-zeta boundary behavior used throughout AF-512--AF-516.
- Hugh L. Montgomery and Robert C. Vaughan, ***Multiplicative Number Theory I: Classical Theory***, Cambridge University Press (2006), DOI `10.1017/CBO9780511618314`, is a standard reference for the prime number theorem and primes in arithmetic progressions.
- Kenneth S. Williams, **“Mertens' Theorem for Arithmetic Progressions,”** *Journal of Number Theory* 6 (1974), 353--359, DOI `10.1016/0022-314X(74)90032-8`, gives the classical Mertens-type arithmetic-progression asymptotics adjacent to `(17)`.
- AF-515 supplies the full-tail proportional-dilation calculation; AF-516 supplies the stability picture around proportional rays.

A focused search did not locate a standard theorem stated specifically as the response law `(6)`--`(7)` for prime-zeta logarithmic curvature after dilating only a PNT-density subfamily of a remote tail. The result should therefore be treated as an exact derived specialization and internal structural classification, not as a literature novelty claim.

## Boundaries and failure modes

1. **PNT density is a regularity hypothesis, not a classification of every sparse set.** A set with no asymptotic density, large blocks or gaps, or scale-dependent density can behave differently.
2. **The zero-density conclusion is scale-specific.** Equation `(8)` says that the leading defect vanishes at `s_A=1+(\log A)^{-k}` for fixed `k>1`; it does not prove uniform relative-curvature invisibility over all `s>1`.
3. **The proportional displacement is coherent.** Selected atoms all use the same fixed factor `c`. Oscillatory factors `c_p`, sign-changing logarithmic displacements, or multiple dilation rays are not classified here.
4. **The theorem uses a fixed source subset `E`.** A selection rule that itself changes with `A` requires a uniform mesoscopic density hypothesis rather than `(1)`.
5. **The arithmetic-progression corollary is classical input.** It supplies explicit controls; it is not evidence that congruence classes are intrinsically privileged by the curvature representation.
6. **No RH consequence is asserted.** The theorem classifies one provenance resource preserved by one prime-derived compression. It does not connect that resource to the zeta-zero discriminator.

## Dependencies

- `AF-514`: broad weighted sublinear tail transports can lose a uniform curvature provenance margin.
- `AF-515`: a cofinite proportional tail dilation creates the mesoscopic gap recovered at `\delta=1`.
- `AF-516`: that full-tail gap is stable under uniformly sublinear rounding around the proportional ray.

## Next theorem-level question

Replace the global density coefficient `(1)` by a **mesoscopic selected-tail profile** adapted to `t_A`. Determine necessary and sufficient conditions on the three selected-tail moments

\[
\sum_{\substack{p>A\\p\in E}}p^{-s_A},
\qquad
\sum_{\substack{p>A\\p\in E}}(\log p)p^{-s_A},
\qquad
\sum_{\substack{p>A\\p\in E}}(\log p)^2p^{-s_A}
\tag{43}
\]

for a nonzero curvature defect. This is the natural boundary for blockwise, oscillatory, or zero-density proportional transports that AF-517 deliberately leaves open.