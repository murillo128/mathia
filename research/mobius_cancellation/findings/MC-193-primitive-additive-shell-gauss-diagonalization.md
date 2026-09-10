# MC-193 — Primitive additive shells are Gauss-diagonal re-encodings of coarse multiplicative sectors

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-192` shows that the additive Fourier transform of the rough primorial residue vector does not remove the hard principal mode: every primitive denominator shell reconstructs the rough Möbius sum, and the denominator-two shell is literally one nonzero additive frequency equal to that sum up to sign.

There is a stronger structural classification of each such shell. For square-free moduli, the primitive additive shell is not merely another set of oscillatory coordinates that happens to contain the zero mode. After coarse-graining the residue vector to the shell denominator, its additive transform is an **invertible Gauss-sum transform that is diagonal in multiplicative characters up to character conjugation**. In particular, the principal multiplicative mode maps to the principal multiplicative mode and never borrows cancellation from nonprincipal sectors.

Let `q` be square-free, let `r|q`, `r>1`, and write

\[
G_m=(\mathbb Z/m\mathbb Z)^\times.
\tag{1}
\]

For the rough residue vector

\[
A_q(X;v)
:=
\sum_{\substack{n\le X\\ n\equiv v\pmod q}}\mu(n),
\qquad v\in G_q,
\tag{2}
\]

define its pushforward to denominator `r` by

\[
B_{q,r}(X;u)
:=
\sum_{\substack{v\in G_q\\ v\equiv u\pmod r}}A_q(X;v)
=
\sum_{\substack{n\le X\\(n,q)=1\\n\equiv u\pmod r}}\mu(n),
\qquad u\in G_r.
\tag{3}
\]

The primitive additive shell of `MC-192` is exactly

\[
E_{q,r}(a;X)
:=
\sum_{u\in G_r}B_{q,r}(X;u)e\!\left(\frac{au}{r}\right)
=
\sum_{\substack{n\le X\\(n,q)=1}}
\mu(n)e\!\left(\frac{an}{r}\right),
\qquad a\in G_r.
\tag{4}
\]

For a Dirichlet character `chi` on `G_r`, use normalized multiplicative Fourier coefficients

\[
\widehat B_{q,r}(\chi)
=
\frac1{\varphi(r)}\sum_{u\in G_r}B_{q,r}(u)\overline{\chi(u)},
\tag{5}
\]

and similarly for `E_{q,r}`. Let

\[
\tau_r(\chi)
:=
\sum_{u\in G_r}\chi(u)e\!\left(\frac ur\right)
\tag{6}
\]

be the ordinary Dirichlet Gauss sum. Then the shell transform satisfies the exact character law

\[
\boxed{
\widehat E_{q,r}(\overline\chi)
=
\tau_r(\chi)\widehat B_{q,r}(\chi).
}
\tag{7}
\]

If `f_chi` is the conductor of `chi`, and `chi*` is the primitive character modulo `f_chi` inducing it, the classical induced-character Gauss-sum formula gives

\[
\tau_r(\chi)
=
\mu\!\left(\frac r{f_\chi}\right)
\chi^*\!\left(\frac r{f_\chi}\right)
\tau_{f_\chi}(\chi^*).
\tag{8}
\]

Because `r` is square-free, `(f_chi,r/f_chi)=1` and `r/f_chi` is square-free. Hence every factor in `(8)` is nonzero and

\[
\boxed{
|\tau_r(\chi)|=\sqrt{f_\chi}>0.
}
\tag{9}
\]

Therefore the map

\[
K_r:B\mapsto
\left(a\mapsto\sum_{u\in G_r}B(u)e(au/r)\right)
\tag{10}
\]

is invertible on `L^2(G_r)`. With normalized `L^2` norm its exact singular spectrum is

\[
\boxed{
\{\sqrt{f_\chi}:\chi\in\widehat G_r\}.
}
\tag{11}
\]

Equivalently,

\[
\boxed{
\|K_rB\|_2^2
=
\sum_{\chi\in\widehat G_r}
f_\chi\,|\widehat B(\chi)|^2.
}
\tag{12}
\]

Thus the primitive additive shell is a lossless, explicitly conditioned re-encoding of the coarse residue vector `B_{q,r}`. It does **not** create an off-diagonal bridge between its multiplicative character sectors.

The relation to the original modulus `q` is equally exact. Let

\[
\pi:G_q\to G_r
\tag{13}
\]

be reduction, and inflate `chi` to `\widetilde\chi=\chi\circ\pi`. Since every fiber of `pi` has size `\varphi(q)/\varphi(r)`, equation `(3)` gives

\[
\widehat B_{q,r}(\chi)
=
\frac{\varphi(q)}{\varphi(r)}
\widehat A_q(\widetilde\chi).
\tag{14}
\]

Combining `(7)` and `(14)`,

\[
\boxed{
\widehat E_{q,r}(\overline\chi)
=
\tau_r(\chi)
\frac{\varphi(q)}{\varphi(r)}
\widehat A_q(\widetilde\chi).
}
\tag{15}
\]

So the denominator-`r` shell sees **only** those `q`-character sectors inflated from `G_r`; each surviving sector is sent to its conjugate with one nonzero Gauss multiplier. This is the composition of the quotient-sector selection already isolated in `MC-191` with an invertible shell-local character transform.

For the principal character `1`, `f_1=1` and `(8)` gives

\[
\tau_r(1)=\mu(r).
\tag{16}
\]

Moreover

\[
\widehat B_{q,r}(1)
=
\frac{G_q(X)}{\varphi(r)},
\qquad
G_q(X)=\sum_{\substack{n\le X\\(n,q)=1}}\mu(n).
\tag{17}
\]

Hence `(7)` becomes

\[
\boxed{
\widehat E_{q,r}(1)
=
\mu(r)\frac{G_q(X)}{\varphi(r)}.
}
\tag{18}
\]

Multiplying by `\varphi(r)` recovers exactly the Ramanujan shell identity of `MC-192`:

\[
\sum_{a\bmod r}^{*}E_{q,r}(a;X)
=
\mu(r)G_q(X).
\tag{19}
\]

The zero mode is therefore not hidden somewhere among unrelated additive frequencies. **Inside every primitive denominator shell it is precisely the multiplicative constant mode in the numerator variable `a`.**

For `r=q`, the pushforward `(3)` is the identity. Consequently, when `q` is square-free, the additive Fourier coefficients at unit frequencies alone,

\[
\left\{
\sum_{v\in G_q}A_q(v)e(av/q):a\in G_q
\right\},
\tag{20}
\]

already determine the complete unit-supported residue vector `A_q` invertibly. No nonunit additive frequencies are required for information recovery.

This sharpens the obstruction after `MC-190`--`MC-192`: **switching from Dirichlet characters to primitive rational additive phases does not escape character-sector separation. On each denominator shell, the apparent additive representation is a Gauss-weighted permutation of the same coarse multiplicative sectors.**

## 1. Gauss diagonalization is exact

Expand `B=B_{q,r}` in multiplicative characters:

\[
B(u)
=
\sum_{\chi\in\widehat G_r}\widehat B(\chi)\chi(u).
\tag{21}
\]

For `a\in G_r`, multiplication by `a` permutes `G_r`. Therefore

\[
\begin{aligned}
K_r\chi(a)
&=
\sum_{u\in G_r}\chi(u)e(au/r)\\
&=
\overline{\chi(a)}
\sum_{v\in G_r}\chi(v)e(v/r)\\
&=
\tau_r(\chi)\overline{\chi(a)}.
\end{aligned}
\tag{22}
\]

Substituting `(21)` into `(10)` gives

\[
K_rB(a)
=
\sum_\chi
\tau_r(\chi)\widehat B(\chi)\overline{\chi(a)}.
\tag{23}
\]

Character orthogonality immediately yields `(7)`.

There is also an equivariance statement that makes the absence of mixing conceptual rather than accidental. On the source define

\[
(T_bB)(u)=B(b^{-1}u),
\qquad b\in G_r,
\tag{24}
\]

and on the additive numerator variable define

\[
(S_bE)(a)=E(ab).
\tag{25}
\]

A change of variables gives

\[
\boxed{K_rT_b=S_bK_r.}
\tag{26}
\]

Thus `K_r` is an intertwiner between the regular multiplicative action and its contragredient realization on additive numerators. Characters diagonalize both actions; `(22)` is the corresponding intertwining multiplier. The additive kernel has not broken unit-group symmetry—it has moved that symmetry to the frequency labels.

## 2. Square-free shells are exactly the nondegenerate regime

For a general modulus, an imprimitive character can have zero Gauss sum. Equation `(8)` shows the two classical failure mechanisms: `r/f_chi` can contain a square factor, giving `mu(r/f_chi)=0`, or it can share a prime with the conductor, giving `chi*(r/f_chi)=0`.

Neither can happen for square-free `r`. Hence every character multiplier is nonzero and `(11)` follows from the primitive identity

\[
|\tau_{f_\chi}(\chi^*)|=\sqrt{f_\chi}.
\tag{27}
\]

This makes the primorial setting particularly rigid. Every divisor denominator of the active primorial is square-free, so every primitive additive shell is a nondegenerate Gauss transform of its coarse unit-group data.

The principal sector is the least-amplified sector: its conductor is `1`, so its singular value is exactly `1`. Higher-conductor sectors can be amplified by up to the square root of their conductor. This explains a potential visual or norm illusion: raw additive-shell energy can be dominated by transverse high-conductor structure even though the principal component remains present exactly and independently.

In particular, from `(12)` and `(18)`,

\[
\|E_{q,r}\|_2^2
=
\frac{|G_q(X)|^2}{\varphi(r)^2}
+
\sum_{\chi\ne1}f_\chi|\widehat B_{q,r}(\chi)|^2.
\tag{28}
\]

The two resources are additive and orthogonal. Strong control of the second term does not force the first to be small.

## 3. This refines the reconstruction-cost interpretation in MC-192

`MC-192` derives the safe inequalities

\[
\max_a|E_{q,r}(a;X)|
\ge
\frac{|G_q(X)|}{\varphi(r)}
\tag{29}
\]

and

\[
|G_q(X)|^2
\le
\varphi(r)
\sum_a^*|E_{q,r}(a;X)|^2.
\tag{30}
\]

Those bounds correctly price recovery when one knows only pointwise magnitudes or an undifferentiated shell norm. Equations `(7)`--`(12)` show that the shell transform itself is not intrinsically information-poor or badly invertible in the square-free setting. The apparent `varphi(r)` cost comes from discarding the multiplicative phase organization across the additive numerators before reconstruction.

Keeping that organization removes the ambiguity completely—but does not produce new cancellation. The principal coefficient of `E` is already `(18)`, so exact inversion simply returns the original rough zero mode.

This separates two failure modes that should not be conflated:

1. **coarse shell projection:** passing from `A_q` to `B_{q,r}` discards `q`-character sectors that do not factor through `G_r`;
2. **additive shell transform:** passing from `B_{q,r}` to `E_{q,r}` loses no information for square-free `r` and only reweights/conjugates its surviving multiplicative sectors.

The second step cannot be the missing principal/transverse coupling because it is exactly diagonal after the correct harmonic decomposition.

## 4. Consequence for the current smooth-primorial frontier

`MC-188` obtains strong arithmetic-progression dispersion transverse to the principal character at the logarithmic primorial. `MC-190` rules out principal/transverse coupling through unit-translation-invariant linear or Hermitian quadratic processing at one modulus. `MC-191` shows that canonical quotient transport through nested primorials remains character-sector diagonal. `MC-192` then tests additive Fourier coordinates and exposes exact low-denominator aliases of the principal rough sum.

The present calculation closes the remaining shell-local ambiguity. Once primitive additive frequencies are grouped by denominator and then analyzed under multiplication of their numerators, they inherit the same sector decomposition. At fixed `r`, any statistic that is invariant under `a\mapsto ab` is again diagonal in the characters of `G_r`; centering away its constant numerator mode removes exactly `(18)` and therefore removes the rough zero mode.

A viable additive/major-minor-arc continuation must consequently contain structure outside this shell-local equivariant category. Examples not ruled out are an ordered or archimedean weight on the numerators that genuinely breaks unit symmetry, a nonlinear arithmetic identity relating different denominators with coefficients not reducible to canonical quotient transport, or a source-side estimate that controls the principal component directly at fixed-power strength. Merely proving stronger cancellation for many individual primitive additive phases, or replacing one shell norm by another unit-invariant quadratic norm, does not create the missing bridge.

## 5. Prior art and novelty assessment

The mathematical engine is classical Dirichlet-character Gauss-sum theory. Montgomery and Vaughan, *Multiplicative Number Theory I: Classical Theory*, Cambridge Studies in Advanced Mathematics 97, Cambridge University Press (2007), Chapter 9, develop primitive characters and Gauss sums; their Theorem 9.10 states the induced-character formula `(8)`. The same book is already retained in this line as `MC-S12` and `MC-S15`. For primitive characters the standard Gauss-sum magnitude is `(27)`.

The finite Fourier identity `(22)` is the classical fact that the additive Fourier transform of a Dirichlet character is its conjugate character times a Gauss sum. No novelty is claimed for `(8)`, `(9)`, `(22)`, character orthogonality, or the singular values as an abstract finite-transform calculation.

The Mathia-specific delta is the application of those classical facts to the exact divisor shells isolated in `MC-192`. It identifies the shell map as `coarse unit-group pushforward -> invertible Gauss transform`, gives the exact conductor-weighted norm ledger `(12)`, and shows that the rough principal coefficient remains a principal coefficient after the additive basis change. A targeted prior-art audit found the component Gauss-sum identities as standard material; no claim is made that this finite harmonic analysis is a new theorem.

## 6. Boundaries and falsification checks

The square-free hypothesis is essential to the blanket invertibility statement. For nonsquarefree `r`, some induced-character Gauss sums can vanish, and the principal Gauss sum is `mu(r)=0`; in that regime `K_r` need not be invertible. The active primorial and all its divisors satisfy the required square-free condition.

Equation `(15)` concerns one primitive denominator shell and canonical reduction from `q` to `r`. It does not rule out a statistic that couples several denominators through genuinely noncanonical arithmetic coefficients, nor does it classify irrational phases. It also does not say that every individual additive twist is as hard as `G_q`; individual high-conductor modes may be substantially easier.

The result is an information-architecture obstruction, not a new Mertens estimate. Invertibility of `K_r` means a full shell retains the coarse data; it does not mean an analytic bound for that shell is cheap. Any proposed gain must still provide an independently proved estimate whose restoration through `(7)`--`(15)` beats the direct rough-Mertens bound rather than merely recoding it.

Finally, the exact orthogonality in `(28)` is specific to the complete unit numerator family. Restricting to a non-invariant subset of numerators can create cross terms, but then the burden shifts to proving that the chosen restriction is source-natural and that its induced mixing yields a quantitative estimate rather than arbitrary symmetry breaking.

## Consequence

The additive escape from the primorial character obstruction is now narrower than `MC-192` alone shows. **For every divisor shell of the square-free primorial, primitive additive phases form an invertible Gauss transform of the coarse multiplicative residue data, with character sector `chi` sent only to `bar chi` and weighted by `sqrt(conductor(chi))`. The rough Möbius zero mode stays the principal sector exactly.**

Therefore a successful fixed-power bridge cannot arise from shell-local Fourier re-encoding or unit-invariant additive energy. It must use genuinely symmetry-breaking arithmetic structure, a noncanonical cross-denominator relation, or an independent fixed-power estimate for the principal rough mode.