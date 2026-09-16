# MC-335 — Low-degree mode dependence cannot approximate endpoint dephasing

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-332` shows that unrestricted mode-dependent coefficients can erase character oscillation pointwise, while `MC-333` and `MC-334` show that rank, Frobenius energy, and cross-mode variation each constrain that escape only when they are controlled quantitatively. There is a separate source-natural complexity measure with a much sharper endpoint threshold: **Boolean Fourier degree of the coefficient dependence on the character mode**.

Continue the exact reciprocal endpoint notation. Let

\[
G=\mathbf F_2^R,
\qquad
\Xi=G\setminus\{0\},
\qquad
N:=2^R,
\qquad
m:=N-1,
\]

and let every shell prime `r` have one-defect sign cell

\[
s(r)\in S:=\{\mathbf1+e_j:1\le j\le R\},
\]

so that

\[
\chi_a(r)=(-1)^{a\cdot s(r)}.
\tag{1}
\]

For a mode-dependent coefficient matrix `W=(w_{a,r})`, assume that for every prime `r` the punctured-cube function

\[
a\mapsto w_{a,r},\qquad a\in\Xi,
\]

admits an extension `\widetilde w_r:G\to\mathbf C` of Walsh-Fourier degree at most `d`. Define the normalized endpoint output

\[
F_W(a)
:=
\frac1A\sum_{r\in\mathcal A}\widetilde w_r(a)(-1)^{a\cdot s(r)},
\qquad a\in G.
\tag{2}
\]

Let

\[
B_d:=\{t\in G:|t|\le d\},
\qquad
\Omega_d:=\bigcup_{s\in S}(s+B_d).
\tag{3}
\]

Then every such output has Walsh support contained in `\Omega_d`. Conversely, because every one-defect cell occurs at the reciprocal endpoint, every Walsh character indexed by `\Omega_d` can be realized by some coefficient family of column degree at most `d`. Hence the possible outputs are **exactly**

\[
\boxed{
\mathcal H_d
=
\operatorname{span}\{\chi_u:u\in\Omega_d\}.
}
\tag{4}
\]

This turns approximate dephasing into an exact punctured-cube approximation problem. Put

\[
D_d:=G\setminus\Omega_d,
\qquad
q_d:=|D_d|-1,
\tag{5}
\]

where `0\in D_d` for every `0\le d\le R-2`. Then

\[
\boxed{
\inf_{F\in\mathcal H_d}
\sum_{a\in\Xi}|F(a)-1|^2
=
\frac{Nq_d}{q_d+1}.
}
\tag{6}
\]

For `1\le d\le R-2`, the shifted Hamming balls have the particularly simple union

\[
\boxed{
\Omega_d
=
\{u\in G:|u|\ge R-1-d\},
}
\tag{7}
\]

so

\[
q_d
=
\sum_{k=1}^{R-2-d}\binom Rk.
\tag{8}
\]

At `d=0`, `\Omega_0=S` and `q_0=N-R-1`.

Two consequences are decisive.

First, if

\[
d\le R-3,
\]

then `q_d\ge R`, and `(6)` gives

\[
\boxed{
\frac1m
\inf_{F\in\mathcal H_d}
\sum_{a\ne0}|F(a)-1|^2
\ge
\frac{NR}{(N-1)(R+1)}
=1-O(R^{-1}).
}
\tag{9}
\]

Thus any coefficient architecture whose dependence on the mode has Fourier degree at most `R-3` cannot merely fail to dephase exactly: **its best normalized RMS approximation to uniform dephasing has error asymptotic to one**. In particular every genuinely low-degree class `d=o(R)` is almost orthogonal to the all-mode dephasing target on the punctured cube.

Second, the threshold is sharp for degree alone. At

\[
d=R-2,
\]

one has

\[
\Omega_{R-2}=G\setminus\{0\},
\qquad
q_{R-2}=0,
\]

and exact dephasing on every nonprincipal mode becomes possible. Indeed the function

\[
F_*(a)=
\begin{cases}
-(N-1),&a=0,\\
1,&a\ne0,
\end{cases}
\tag{10}
\]

has Walsh expansion

\[
\boxed{
F_*=-\sum_{u\ne0}\chi_u,
}
\tag{11}
\]

so `F_*\in\mathcal H_{R-2}` and its restriction to `\Xi` is the exact unit target.

Therefore **low Boolean-Fourier degree is a genuine coupling restriction**, unlike bare rank: the endpoint cannot hide a useful approximate matched filter inside `o(R)`-degree mode dependence. But degree alone ceases to protect the problem abruptly at `R-2`; once near-maximal degree is admitted, exact phase erasure returns, potentially with very large coefficient energy or principal-mode spillover. The degree resource must therefore be combined with the energy/variation resources of `MC-333`–`MC-334` if one wants a viable analytic coefficient class rather than another programmable matched filter.

No estimate for `M(x)` follows.

## 1. Multiplying by the endpoint character shifts Fourier support

Write the Walsh expansion of a degree-`d` column extension as

\[
\widetilde w_r(a)
=
\sum_{|t|\le d}\widehat w_r(t)\chi_t(a),
\qquad
\chi_t(a):=(-1)^{a\cdot t}.
\tag{12}
\]

Because `\chi_t\chi_s=\chi_{t+s}`, multiplying by the endpoint character in `(2)` gives

\[
\widetilde w_r(a)\chi_{s(r)}(a)
=
\sum_{|t|\le d}\widehat w_r(t)\chi_{t+s(r)}(a).
\tag{13}
\]

Every resulting frequency lies in the Hamming ball `s(r)+B_d`. Summing over primes proves the support containment in `(4)`.

Conversely, fix `u\in\Omega_d`. By definition there are `s\in S` and `t\in B_d` with `u=s+t`. Choose any shell prime `r` from cell `s`, set all other prime coefficients to zero, and take

\[
\widetilde w_r(a)=A\chi_t(a).
\]

Then the normalized output is exactly `\chi_u(a)`. Linear combinations realize every element of the span in `(4)`. No coefficient-energy bound is imposed in this converse; this is precisely why `(4)` isolates Fourier degree as a resource independently of the Frobenius and variation costs studied earlier.

## 2. The one-defect cells force a high-frequency output band

Let `u\in G` have Hamming weight `k<R`. If `u_j=0`, then for

\[
s_j=\mathbf1+e_j
\]

one has

\[
|u+s_j|=R-1-k.
\tag{14}
\]

Choosing a zero coordinate `j` therefore gives

\[
\min_{s\in S}|u+s|=R-1-k
\qquad(k<R).
\tag{15}
\]

For `u=\mathbf1`, the minimum distance to `S` is `1`. Consequently, when `1\le d\le R-2`, a frequency belongs to `\Omega_d` exactly when its weight is at least `R-1-d`, proving `(7)` and `(8)`.

The case `d=0` is slightly exceptional because the all-one frequency has distance one rather than zero from `S`: then the support is exactly the `R` one-defect frequencies themselves.

This geometry explains why the restriction is strong. A low-degree coefficient function lives near the bottom of the Walsh cube, but multiplication by a one-defect endpoint character translates it to a band near the **top** of the cube. Uniform dephasing on the punctured cube, by contrast, cannot be represented using only that top band without paying for the missing low frequencies.

## 3. Exact punctured-cube approximation formula

Let

\[
D_d=\{0,u_1,\ldots,u_q\},
\qquad q=q_d,
\]

be the missing frequency set. For `F\in\mathcal H_d`, set

\[
e(a):=F(a)-1\quad(a\ne0),
\qquad
z:=F(0)-1.
\tag{16}
\]

Since every Fourier coefficient of `F` on `D_d` vanishes, using unnormalized Walsh sums gives

\[
\sum_{a\ne0}e(a)=-N-z
\tag{17}
\]

for the zero frequency, and

\[
\sum_{a\ne0}e(a)\chi_{u_j}(a)=-z
\qquad(1\le j\le q)
\tag{18}
\]

for the nonzero missing frequencies.

Restrict the missing Walsh characters to `\Xi`. Their Gram matrix is independent of which distinct frequencies were omitted:

\[
\sum_{a\ne0}\chi_u(a)\overline{\chi_v(a)}
=
\begin{cases}
N-1,&u=v,\\
-1,&u\ne v,
\end{cases}
\]

hence

\[
\boxed{
G_D=N I_{q+1}-\mathbf1\mathbf1^*.
}
\tag{19}
\]

Because `\Omega_d` is nonempty, `q+1<N` here and

\[
G_D^{-1}
=
\frac1N I_{q+1}
+
\frac1{N(N-q-1)}\mathbf1\mathbf1^*.
\tag{20}
\]

For fixed `z`, equations `(17)`–`(18)` prescribe the inner products of `e` with these `q+1` restricted characters. The minimum possible squared norm of `e` is therefore the corresponding inverse-Gram quadratic form. Writing

\[
b(z)=(-N-z,-z,\ldots,-z),
\]

one obtains

\[
\min\|e\|_2^2
=b(z)^*G_D^{-1}b(z).
\tag{21}
\]

The right-hand side is minimized at

\[
z=-\frac{N}{q+1},
\tag{22}
\]

and substitution gives exactly

\[
\boxed{
\min\|e\|_2^2
=
\frac{Nq}{q+1}.
}
\tag{23}
\]

These are not merely necessary Fourier constraints. They are sufficient: satisfying `(17)`–`(18)` makes the full-cube function have zero Fourier coefficients on `D_d`, hence places it in `\mathcal H_d`. Thus `(23)` is the exact distance, proving `(6)`.

For `d=R-3`, the missing set is precisely the zero frequency plus the `R` singleton frequencies, so `q=R` and `(9)` is already attained from only the constant and degree-one missing moments. For smaller `d`, many more low frequencies are absent and `(6)` pushes the error still closer to the full target norm.

## 4. Why this is independent of rank, energy, and variation

The restriction here is on **how each prime column may depend on the mode index**. It is not a matrix-rank condition. A low-degree family can have many independent coefficient columns and large rank, while `MC-332`'s matched filter has rank only `R` but column degree `R-1`.

Likewise `(6)` imposes no Frobenius-energy budget. Coefficients may be arbitrarily large. The obstruction survives because the required Walsh frequencies are absent altogether. This is stronger than an energy lower bound inside the degree-`d` class.

At the sharp threshold `d=R-2`, that spectral absence disappears: every nonzero frequency becomes available and `(10)`–`(11)` give exact dephasing. The construction is intentionally not claimed to be energy-efficient or low-variation. This is where `MC-333` and `MC-334` remain necessary: Fourier degree, rank, coefficient energy, and cross-mode variation are distinct resources, and none should be silently substituted for another.

The source-natural interpretation is concrete. If a proposed joint coefficient architecture lets `w_{a,r}` depend on the source-generator selection bits `a_1,\ldots,a_R` only through bounded-order or `o(R)` Walsh interactions, then it lies deep inside the forbidden regime `(9)`. Such an architecture genuinely excludes phase leakage. To recover even approximate all-mode dephasing, the dependence must involve interactions of order almost `R`, or abandon this degree model entirely.

## 5. Prior art and novelty boundary

The underlying harmonic analysis is classical. Walsh characters form the Fourier basis on `\mathbf F_2^R`, multiplication translates Fourier support, and Fourier degree is the maximum Hamming weight of a nonzero coefficient. The same Boolean-Fourier language and Ryan O'Donnell's *Analysis of Boolean Functions* (Cambridge University Press, 2014, DOI `10.1017/CBO9781139814782`) were already audited for `MC-328`; no new claim is made for these facts.

The coding-theory viewpoint is adjacent: low-degree evaluation spaces, puncturing at one cube point, and their dual constraints are standard Reed–Muller themes. Irving S. Reed's original *A class of multiple-error-correcting codes and the decoding scheme* (Transactions of the IRE Professional Group on Information Theory 4 (1954), 38–49, DOI `10.1109/TIT.1954.1057465`) is a classical anchor, while modern Fourier-analytic Reed–Muller work treats the same broad interaction between low-degree structure and Walsh analysis. The present complex-valued Fourier-degree space is not being identified literally with a binary Reed–Muller code; the analogy is only a prior-art boundary.

A targeted literature search on 16 September 2026 found the standard Boolean-Fourier and punctured/shortened Reed–Muller mechanisms, but no need for an external theorem beyond those classical facts. No novelty claim is made for the abstract approximation calculation `(17)`–`(23)`. The durable Mathia delta is its specialization to the exact reciprocal one-defect character frame after `MC-332`–`MC-334`: it gives a sharp degree threshold and exact RMS error for a previously unpriced source-natural mode-dependence class.

## Boundaries and falsification tests

- **Exact one-defect endpoint support is load-bearing.** The translated support set `\Omega_d` comes from `s(r)\in\{\mathbf1+e_j\}`. A different sign-cell geometry can have a very different degree threshold.
- **Equal cell multiplicities are not needed for the obstruction.** Support containment uses only the one-defect cells. The converse realization of all of `\mathcal H_d` needs every cell to occur at least once, which the reciprocal endpoint supplies.
- **Extension degree is the definition.** Coefficients live originally on `\Xi`; saying they have degree at most `d` means each punctured column admits a full-cube extension of that degree. This avoids assigning a noncanonical Fourier transform directly to the punctured cube.
- **The target is spread across all nonprincipal modes.** Sparse target families can have different approximation geometry and remain a separate audit surface.
- **No coefficient-norm control is used.** Once `d=R-2`, exact dephasing is possible, but `(10)` has a principal-mode spike and the realizing coefficients may be expensive. Energy and variation controls remain independent.
- **No analytic family theorem is proved.** The result only shows that low-degree mode dependence is a nontrivial admissible class. It does not show that Schlage-Puchta or another prime-family estimate improves for that class.
- **No circular zero information enters.** The proof is finite Walsh analysis on the already-derived endpoint frame.
- **No RH-scale conclusion is claimed.** This is a method-boundary theorem for the live joint-coefficient route.

## Consequence for the research line

The vague requirement from `MC-332` that mode dependence be "structured" now has a concrete candidate with real teeth: **bounded-order dependence on the mode bits cannot secretly contain an approximate matched filter.** In fact any `d=o(R)` column-degree architecture misses the uniform endpoint target by essentially its full `L^2` norm.

This does not yet create an arithmetic gain. The next useful analytic question is narrower and falsifiable: whether a prime-family mean-square or higher-order estimate can exploit a coefficient matrix whose mode columns have degree `d=o(R)` (or another comparable source-natural complexity restriction) without first relaxing back to unrestricted rowwise coefficients. Any such theorem would combine a class that provably excludes endpoint dephasing with an analytic estimate sensitive to the same class, rather than paying for a matched filter that the endpoint can program.