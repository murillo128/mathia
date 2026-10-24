# PC-449 — Equivalent power weights give cotangent towers empty resolvent

**Status:** EXACT-DERIVED + CLASSICAL-STRUCTURE + NEGATIVE/OBSTRUCTION + CONTROL-BLIND. An explicit probability equivalent to Haar, with density bounded below and integrable but unbounded above, makes the unchanged singleton-base complete cotangent tower closable while every closed extension has spectrum equal to the whole complex plane. The canonical closure still has a dense span of real-eigenvalue eigenvectors. Thus PC-446's inherited-band inclusion can be maximally strict even without a singular measure or failure of closability. This is an operator-domain counterexample, not a prime discriminator or an RH mechanism.

## 1. Exact tower, density and theorem

Take the base $P_2^*=\{-1\}$, with coherent lift coordinates
\[
y_t^{(m)}=e^{2\pi i(1/2+t)/m},\qquad 0\le t<m.
\]
The complete power-preimage inverse limit is $X\simeq\widehat{\mathbb Z}$. Let $\mu$ be Haar probability and $\mathcal A_{\rm cyl}$ the algebra of functions factoring through some $X\to\mathbb Z/m\mathbb Z$. Retain the exact PC-443 action
\[
(B_m)_{ts}=\begin{cases}
\dfrac{i}{m}\cot\dfrac{\pi(t-s)}m,&t\ne s,\\
0,&t=s,
\end{cases}
\qquad B_m^+=B_m+J_m/m.
\tag{1}
\]
Both are compatible with all power-map pullbacks. On Haar space they have norm one and spectrum $[-1,1]$. For $\chi_q(x)=e^{2\pi i j(x\bmod m)/m}$, $q=j/m\in[0,1)\cap\mathbb Q$, their pointwise action is
\[
\mathcal B\chi_q=b(q)\chi_q,\qquad
b(0)=0,\quad b(q)=1-2q\ (0<q<1).
\tag{2}
\]
The augmented action changes only $b(0)$ to $b^+(0)=1$.

Fix any prime $p$ and $0<\alpha<1$. Write $x_p$ for the $p$-adic coordinate, and define
\[
c_\alpha=\frac{1-p^{\alpha-1}}{1-p^{-1}},\qquad
w_\alpha(x)=c_\alpha p^{\alpha v_p(x_p)},\qquad
\nu_\alpha=w_\alpha\mu.
\tag{3}
\]
Assign any positive finite value on the null set $x_p=0$. The geometric series
\[
\int p^{\alpha v_p(x_p)}\,d\mu
=(1-p^{-1})\sum_{j\ge0}p^{(\alpha-1)j}=c_\alpha^{-1}
\tag{4}
\]
shows that $\nu_\alpha$ is a probability equivalent to Haar, with $w_\alpha\ge c_\alpha>0$ almost everywhere and no finite essential upper bound.

**Theorem.** On $H_\alpha=L^2(X,\nu_\alpha)$, for either raw cylinder prescription:

1. The cylinder operator is densely defined and closable. A densely defined closed extension exists.
2. Every closed extension $T$ retaining all cylinder functions and their action has
\[
\boxed{\rho(T)=\varnothing,\qquad\sigma(T)=\mathbb C.}
\tag{5}
\]
3. For the canonical graph closure and the Haar-action maximal extension defined below, every $\lambda\notin[-1,1]$ is continuous spectrum: $T-\lambda$ is injective with dense, nonsurjective range. Their point spectra are exactly
\[
\sigma_p(T)=\mathbb Q\cap(-1,1)
\quad\text{or}\quad
(\mathbb Q\cap(-1,1))\cup\{1\}
\tag{6}
\]
for the unaugmented or augmented prescription, respectively. The characters span a dense subspace in either case.

The density in (3) is an explicitly chosen control, not a geometry-forced arithmetic law. A single-base counterexample suffices to rule out a general extension of PC-444's bounded-similarity conclusion to unbounded equivalent densities.

## 2. A closed realization exists

Let $B_\mu$ denote the appropriate bounded Haar operator. Since $w_\alpha\ge c_\alpha$, the identity embedding $H_\alpha\hookrightarrow L^2(\mu)$ is continuous and injective. Define
\[
D(T_{\max})=\{f\in H_\alpha:B_\mu f\in H_\alpha\},
\qquad T_{\max}f=B_\mu f.
\tag{7}
\]
Every cylinder function and its image is bounded, hence belongs to $H_\alpha$. Cylinder functions are dense because they are uniformly dense in $C(X)$, which is dense for any finite Borel measure on this compact metrizable space.

If $f_n\to f$ and $T_{\max}f_n\to g$ in $H_\alpha$, both limits hold in $L^2(\mu)$. Boundedness of $B_\mu$ gives $g=B_\mu f$. Thus $f\in D(T_{\max})$, and $T_{\max}$ is closed. In particular the cylinder restriction is closable, with graph closure $T_{\min}\subseteq T_{\max}$. No equality of these two domains is needed or asserted.

This separates the present example from PC-447--PC-448: the operator exists. Its subsequent spectral failure cannot be attributed to a nonexistent closure.

## 3. Every off-band resolvent is forced to be unbounded

For $m=p^k$, let $E_{k,t}=\{x:x\equiv t\pmod{p^k}\}$. Equation (3) gives the exact marginal masses
\[
\nu_\alpha(E_{k,0})=p^{(\alpha-1)k},\qquad
\nu_\alpha(E_{k,n})=c_\alpha p^{\alpha v_p(n)-k}
\quad(k>v_p(n),\ n\ne0).
\tag{8}
\]
In the second formula $n$ is any fixed nonzero ordinary integer, reduced modulo $p^k$. The first follows by summing (4) starting at $j=k$; the second uses the constant valuation on that residue cylinder. Therefore
\[
\frac{\nu_\alpha(E_{k,0})}{\nu_\alpha(E_{k,n})}
=c_\alpha^{-1}p^{\alpha(k-v_p(n))}\longrightarrow\infty.
\tag{9}
\]

Fix $\lambda\in\mathbb C\setminus[-1,1]$. At each finite level the matrix $B_m^{(+)}-\lambda I$ is invertible. In the pointwise basis its inverse entry is
\[
a_{m,n}^{(+)}(\lambda)
=\big[(B_m^{(+)}-\lambda I)^{-1}\big]_{0,n}
=\frac1m\sum_{j=0}^{m-1}
\frac{e^{-2\pi ijn/m}}{b^{(+)}(j/m)-\lambda}.
\tag{10}
\]
For each fixed integer $n$, ordinary Riemann sums imply
\[
a_{m,n}^{(+)}(\lambda)\longrightarrow
a_n(\lambda):=\int_0^1\frac{e^{-2\pi inq}}{1-2q-\lambda}\,dq.
\tag{11}
\]
The altered value at $j=0$ contributes only $O_\lambda(m^{-1})$; this includes the unaugmented midpoint value. There is no pole on $[0,1]$ because $\lambda\notin[-1,1]$.

For every such $\lambda$, **some nonzero integer $n=n(\lambda)$ has $a_n(\lambda)\ne0$**. Otherwise Fourier uniqueness in $L^2(0,1)$ would make the function $(1-2q-\lambda)^{-1}$ constant almost everywhere, contrary to its nonzero derivative. The selected $n$ may depend on $\lambda$; no fixed coefficient is assumed nonzero everywhere.

Suppose $T$ is any closed extension and $\lambda\in\rho(T)$. For every level-$m$ cylinder $h$, the cylinder solution
$u=(B_m^{(+)}-\lambda I)^{-1}h$ obeys $(T-\lambda)u=h$. Injectivity forces $u=(T-\lambda)^{-1}h$. Test this identity on $h=\mathbf1_{E_{k,n}}$, and retain just the output norm on $E_{k,0}$. Equations (9)--(11) imply
\[
\begin{split}
\|(T-\lambda)^{-1}\|
&\ge |a_{p^k,n}^{(+)}(\lambda)|
\sqrt{\frac{\nu_\alpha(E_{k,0})}{\nu_\alpha(E_{k,n})}}\\
&=|a_{p^k,n}^{(+)}(\lambda)|\,c_\alpha^{-1/2}
p^{\alpha(k-v_p(n))/2}\longrightarrow\infty.
\end{split}
\tag{12}
\]
This contradicts boundedness of a resolvent. It does not assume convergence of operators on different Hilbert spaces or infer infinite spectrum from finite spectra alone: all finite-level tests use subspaces of the **same** $H_\alpha$ and the forced inverse of the proposed $T$.

All rational character eigenvalues in (2) survive in any extension, since the characters have norm one under every probability. Their closure is $[-1,1]$. Closedness of the spectrum therefore excludes every band point from the resolvent as well. Together with (12), this proves (5). Every such extension is necessarily unbounded.

## 4. Dense eigenvectors, continuous spectrum and small measure changes

For $T_{\min}$ or $T_{\max}$, equation (7) implies that an eigenvector must also be a Haar eigenvector. Haar Fourier diagonalization (2) supplies no eigenvalues beyond (6), and all characters already lie in the cylinder domain. This proves (6) and completeness of their linear span. Completeness here is not a Riesz-basis or self-adjoint spectral-type assertion.

For $\lambda\notin[-1,1]$, the same embedding makes $T_{\min}-\lambda$ and $T_{\max}-\lambda$ injective. Their ranges contain every cylinder function, by the finite inverse in (10), and are dense. They cannot be surjective: a closed bijection onto the Hilbert space would have a bounded inverse, contradicting (12). Thus every off-band point is continuous spectrum for these two realizations. This classification is not extended to arbitrary larger closed extensions.

Moreover,
\[
\|w_\alpha-1\|_{L^1(\mu)}\longrightarrow0
\quad(\alpha\downarrow0).
\tag{13}
\]
Indeed $c_\alpha\to1$, $p^{\alpha v}\to1$ at every finite valuation, and for $0<\alpha\le\alpha_0<1$ the integrable function $1+p^{\alpha_0v}$ dominates the difference. Thus $\nu_\alpha\to\mu$ in total variation, while every positive $\alpha$ has (5) and Haar has spectrum $[-1,1]$. There is no total-variation neighborhood of Haar on which closable unchanged-action realizations retain the Haar spectrum, even when restricting to equivalent probabilities bounded below. PC-444's two-sided bounded-density hypothesis is doing real work.

## 5. Classical mechanism, controls and validation

The singleton action itself is the standard ergodic Hilbert transform of the profinite translation $S f(x)=f(x+1)$: on cylinders,
\[
\mathcal B f=\frac1{\pi i}\lim_{N\to\infty}
\sum_{0<|n|\le N}\frac{S^nf}{n}.
\tag{14}
\]
To verify this, apply the symmetric sum to each of the finitely many characters of a cylinder function. The classical sawtooth Fourier series gives $1-2q$ for $0<q<1$ and zero at $q=0$, exactly (2). The augmented operator adds Haar averaging. No weighted-space convergence theorem is inferred from (14) beyond cylinders.

The sawtooth identity is the first Bernoulli Fourier series, [DLMF §24.8](https://dlmf.nist.gov/24.8). Weighted ergodic Hilbert transforms are classical: E. Atencia and F. J. Martín-Reyes, *The maximal ergodic Hilbert transform with weights*, Pacific J. Math. **108** (1983), 257–263, [journal text](https://msp.org/pjm/1983/108-2/pjm-v108-n2-p01-s.pdf), characterize maximal-transform boundedness by an orbit weight condition. That theorem does not by itself classify the closed raw tower's spectrum; (8)--(12) prove the needed conclusion directly.

Closed operators with empty resolvent are also established operator theory; see P. Binding and V. Strauss, *On Operators with Spectral Square but without Resolvent Points*, Canad. J. Math. **57** (2005), 61–81, [DOI 10.4153/CJM-2005-003-4](https://doi.org/10.4153/CJM-2005-003-4). Their different spectral-square hypotheses are not assumed here. Graph closure and the closed-graph inverse argument use standard theory, e.g. E. Kowalski, *Spectral theory in Hilbert spaces*, §§4.2 and 4.5, [author's notes](https://people.math.ethz.ch/~kowalski/spectral-theory.pdf).

The bounded literature audit covered weighted ergodic/discrete Hilbert transforms, unbounded changes of Hilbert norm and empty-resolvent operators. No novelty is claimed for those abstract phenomena or (14). The local mathematical delta is an **explicit equivalent probability for the unchanged cotangent tower**, an actual closed realization, and the all-extension finite-inverse obstruction (12). This differs from PC-364's one-sided raising operator and residual-spectrum mechanism, and from PC-448's mixed singular measure with no closure.

Replacing the singleton base by any point at an irrational angle leaves every difference $(t-s)/m$ in (1) unchanged. The same probability on the lift coordinates gives exactly the same result. The prime $p$ selects a coordinate of the control density; it does not discriminate prime birth. The weight depends on a chosen coherent origin and is not asserted to be invariant under arbitrary fiber relabelling.

**Validation.** The infinite claims are proved above. Separate pure-Python complex-arithmetic diagnostics checked (2) directly at $m=3,4,8,16,31$, with maximum eigenvector residual $2.7\times10^{-14}$. Gaussian elimination of both finite inverses at $\lambda=i,2,1+i/2$ agreed with the entry formula (10) to $3.3\times10^{-16}$. The masses in (8) summed to one and respected refinement for $p=2,3,5$, $\alpha=0.2,0.5,0.8$, and $1\le k\le4$, with maximum refinement residual $1.2\times10^{-16}$. For $p=2,\alpha=1/2,\lambda=i,n=1$, the lower bound in (12) was approximately $1.256,1.807,2.567,3.634$ at $m=64,256,1024,4096$. These are finite diagnostics, not proofs of divergence or of the nonzero coefficient for every complex parameter. The decisive audit points are the positive lower density bound, the unequal cylinder masses, Fourier uniqueness with a parameter-dependent $n$, and uniqueness of the forced finite inverse inside any hypothetical global resolvent.

This finding classifies the explicit family (3), not every unbounded density. It does not change the kernel, discard cylinder functions, or use half-density compensation. PC-444's compensated operator remains bounded and unitarily equivalent to Haar even for (3). No RH implication, all-base theorem or general classification of weighted closed realizations follows.
